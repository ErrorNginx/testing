FROM apache/airflow:2.8.2
ADD requirements.txt .
# RUN pip install dbt-core
RUN pip install dbt-bigquery
RUN pip install apache-airflow==${AIRFLOW_VERSION} -r requirements.txt