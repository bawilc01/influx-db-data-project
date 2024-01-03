from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('path/to/.env')
load_dotenv(dotenv_path=dotenv_path)
from datetime import datetime

from influxdb_client import WritePrecision, InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

url = 'https://us-west-2-1.aws.cloud2.influxdata.com'
token = 'my-token'
org = 'my-org'
bucket = 'my-bucket'

with InfluxDBClient(url=url, token=token, org=org) as client:
    p = Point("weatherstation") \
        .tag("location", "San Francisco") \
        .field("temperature", 25.9) \
        .time(datetime.utcnow(), WritePrecision.MS)

    with client.write_api(write_options=SYNCHRONOUS) as write_api:
        write_api.write(bucket=bucket, record=p)
