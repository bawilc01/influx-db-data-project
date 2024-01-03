from influxdb_client import InfluxDBClient
import os
from dotenv import load_dotenv

INFLUX_TOKEN = os.getenv('INFLUX_TOKEN')
INFLUX_ORG = os.getenv('INFLUX_ORG')
INFLUX_BUCKET = os.getenv('INFLUX_BUCKET')
INFLUX_URL = os.getenv('INFLUX_URL')
load_dotenv()

url = INFLUX_URL
token = INFLUX_TOKEN
org = INFLUX_ORG
bucket = INFLUX_BUCKET

with InfluxDBClient(url=url, token=token, org=org) as client:
    query_api = client.query_api()

    tables = query_api.query('from(bucket: "my-bucket") |> range(start: -1d)')

    for table in tables:
        for record in table.records:
            print(str(record["_time"]) + " - " + record.get_measurement()
                  + " " + record.get_field() + "=" + str(record.get_value()))
