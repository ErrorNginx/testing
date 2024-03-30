from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

# let's setup arguments for our dag

my_dag_id = "my_first_dag"

default_args = {
    'owner': 'proton',
    'depends_on_past': False,
    'retries': 10,
    'concurrency': 1
}

# dag declaration

dag = DAG(
    dag_id=my_dag_id,
    default_args=default_args,
    start_date=datetime(2019, 6, 17),
    schedule_interval='@once'
)


# Here's a task based on Bash Operator!

bash_task = BashOperator(task_id='bash_task_1',
        bash_command="cd /opt/airflow/dbt/credit_card_dwh && dbt deps && dbt seed --profiles-dir .",
        dag=dag
    )

bash_task_dua = BashOperator(task_id='bash_task_2',
        bash_command="cd /opt/airflow/dbt/credit_card_dwh && dbt run --profiles-dir .",
        dag=dag
    )


bash_task >> bash_task_dua