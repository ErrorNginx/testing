import pyarrow.csv as pv
import pyarrow.parquet as pq
import logging

def format_to_parquet(src_file):
    if not src_file.endswith('.csv'):
        logging.error("Can only accept source files in CSV format, for the moment")
        return
    table = pv.read_csv(src_file)
    pq.write_table(table, src_file.replace('.csv', '.parquet'))

def csv_to_parquet(**kwargs):
    src_files = kwargs.get('src_files', [])
    for src_file in src_files:
        format_to_parquet(src_file)