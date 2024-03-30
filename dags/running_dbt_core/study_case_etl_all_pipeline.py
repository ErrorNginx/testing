import os
import pendulum
from airflow import DAG
from datetime import timedelta
from airflow.models.variable import Variable
from airflow.operators.python_operator import PythonOperator
from airflow.providers.google.cloud.operators.gcs import GCSDeleteObjectsOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryCreateExternalTableOperator
from airflow.operators.bash import BashOperator
from utils.schema import table1_schema, table1_schema_raw_credit_card
from utils.local_to_gcs import upload_to_gcs
from utils.fetch_mysql import fetch_data_task
from utils.csv_to_parquet import format_to_parquet

# Konfigurasi
BASE_PATH = Variable.get("BASE_PATH")
BUCKET = 'test_location_agus' 
PROJECT_ID = 'forward-entity-411314'
BIGQUERY_DATASET = 'test_location'
SQL_FILE_PATH = os.path.join(os.path.dirname(__file__), 'query_all.sql')

# Default args
default_args = {
    'owner': 'Agus mahari',
    'start_date': pendulum.datetime(2024, 3, 15, tz='Asia/Jakarta'),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

# Inisialisasi DAG
with DAG(
    'study_case_etl_all_pipeline',
    default_args=default_args,
    description='A simple DAG to demonstrate MySql hook in Airflow',
    dagrun_timeout=timedelta(minutes=2),
    schedule_interval='@once',
    tags=['daily', 'gcs', 'bigquery', 'dbt'],
) as dag:
    # Task untuk mengambil data dari MySQL
    fetch_data_task_id = PythonOperator(
        task_id='fetch_data_task_id',
        python_callable=fetch_data_task,
        op_kwargs={
            'output_file': '/opt/airflow/data/{{ task.task_id }}_{{ ds }}.csv'
            
        },
    )

    # Task untuk mengonversi CSV menjadi Parquet
    format_to_parquet_task = PythonOperator(
        task_id="format_to_parquet_task",
        python_callable=format_to_parquet,
        op_kwargs={
            'src_file': '/opt/airflow/data/fetch_data_task_id_{{ ds }}.csv',
        },
    )

    # Task untuk mengunggah data ke GCS
    local_to_gcs_task = PythonOperator(
        task_id="local_to_gcs_task",
        python_callable=upload_to_gcs,
        op_kwargs={
            "bucket": BUCKET,
            "object_name": "raw/raw_credit_card/raw_credit_card_{{ ds }}.parquet",
            "local_file": "/opt/airflow/data/fetch_data_task_id_{{ ds }}.parquet",
        },
    )

    # Task untuk membuat tabel eksternal di BigQuery
    bigquery_external_table_task = BigQueryCreateExternalTableOperator(
        task_id="bigquery_external_table_task",
        table_resource={
            "tableReference": {
                "projectId": PROJECT_ID,
                "datasetId": BIGQUERY_DATASET,
                "tableId": "raw_credit_card",
            },

            "schema": table1_schema_raw_credit_card,

            "externalDataConfiguration": {
                "autodetect": "False",
                "sourceFormat": "PARQUET",
                "sourceUris": [f"gs://{BUCKET}/raw/raw_credit_card/*.parquet"],
                "compression": "GZIP",
                "clustering": {
                    "fields": ["id"]
                },
            },

            
        },
    )


    task_dbt_run = BashOperator(task_id='bash_task_2',
        bash_command="cd /opt/airflow/dbt/credit_card_dwh && dbt run --profiles-dir .",
        dag=dag
    )

    # Task untuk menghapus file Parquet yang sudah tidak diperlukan di GCS
    delete_gcs_parquet_task = GCSDeleteObjectsOperator(
        task_id="delete_gcs_parquet_task",
        bucket_name=BUCKET,
        objects=["raw/raw_credit_card/raw_credit_card_{{ ds }}.parquet"],
    )

    # Task untuk menghapus file CSV yang sudah tidak diperlukan
    delete_dataset_csv_task = BashOperator(
        task_id="delete_dataset_csv_task",
        bash_command="rm -rf /opt/airflow/data/fetch_data_task_id_{{ ds }}.csv",
    )

    # Task untuk menghapus file Parquet yang sudah tidak diperlukan
    delete_dataset_parquet_task = BashOperator(
        task_id="delete_dataset_parquet_task",
        bash_command="rm -rf /opt/airflow/data/fetch_data_task_id_{{ ds }}.parquet",
    )

    # Pengaturan dependensi antar task
    fetch_data_task_id >> format_to_parquet_task >> local_to_gcs_task >> bigquery_external_table_task
    bigquery_external_table_task >> task_dbt_run >> [delete_gcs_parquet_task, delete_dataset_csv_task, delete_dataset_parquet_task]
