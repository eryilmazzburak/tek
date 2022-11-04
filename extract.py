from google.cloud import bigquery
import os


SERVICE_ACCOUNT_JSON = os.environ["GOOGLE_APPLICATION_CREDENTIALS"]
client = bigquery.Client()


def bq_to_csv():
      query = """
                  SELECT
                  vendor_id, pickup_location_id, dropoff_location_id, pickup_datetime, dropoff_datetime
                  FROM
                  bigquery-public-data.new_york_taxi_trips.tlc_green_trips_2014
                  where data_file_year = 2014
                  and data_file_month = 3
                  and pickup_datetime > '2014-03-01'
                  and dropoff_datetime < '2014-03-08';
                  """

      df = client.query(query).to_dataframe()
      df.to_csv("/Users/burakyilmaz/Desktop/teknasyon/extracted_data.csv", index=False, header=True)
      print("csv file generated")
bq_to_csv()