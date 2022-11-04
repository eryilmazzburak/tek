from google.cloud import bigquery
import os

# Construct a BigQuery client object.
client = bigquery.Client()



table_id = "teknasyon.one.two"

job_config = bigquery.LoadJobConfig(
    schema=[
        bigquery.SchemaField("vendor_id", "INTEGER"),
        bigquery.SchemaField("pickup_location_id", "INTEGER"),
        bigquery.SchemaField("dropoff_location_id", "INTEGER"),
        bigquery.SchemaField("pickup_datetime", "DATETIME"),
        bigquery.SchemaField("dropoff_datetime", "DATETIME"),
    ],
    skip_leading_rows=1,
    source_format=bigquery.SourceFormat.CSV,
)

uri = "gs://teknasyon/extracted_data.csv"
load_job = client.load_table_from_uri(
    uri, table_id, job_config=job_config
)  # Make an API request.

load_job.result()  # Waits for the job to complete.

destination_table = client.get_table(table_id)  # Make an API request.
print("Loaded {} rows.".format(destination_table.num_rows))