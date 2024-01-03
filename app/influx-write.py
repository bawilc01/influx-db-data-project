from datetime import datetime
import os
from dotenv import load_dotenv

from influxdb_client import WritePrecision, InfluxDBClient, Point, WriteOptions
from influxdb_client.client.write_api import SYNCHRONOUS
from influxdb_client.client.write_api import ASYNCHRONOUS

INFLUX_TOKEN = os.getenv('INFLUX_TOKEN')
INFLUX_ORG = os.getenv('INFLUX_ORG')
INFLUX_BUCKET = os.getenv('INFLUX_BUCKET')
INFLUX_URL = os.getenv('INFLUX_URL')
load_dotenv()

url = INFLUX_URL
token = INFLUX_TOKEN
org = INFLUX_ORG
bucket = INFLUX_BUCKET

from influxdb_client import InfluxDBClient
client = InfluxDBClient(url="http://localhost:9999", token=token, org=org)

# instantiate the write api
write_api = client.write_api()

write_api.write(bucket, org, [{"measurement": "h2o_feet", "tags": {"location": "coyote_creek"}, "fields": {"water_level": 1}, "time": 1}])
write_api_sync = client.write_api(write_options=SYNCHRONOUS)
write_api_async = client.write_api(write_options=ASYNCHRONOUS)

# batching write options
"""
The default instance of WriteApi uses batching. You can specify the following batch parameters:

batch_size: the number of data points to collect in a batch
flush_interval: the number of milliseconds before the batch is written
jitter_interval: the number of milliseconds to increase the batch flush interval by a random amount
retry_interval: the number of milliseconds to retry unsuccessful write. The retry interval is used when the InfluxDB server does not specify “Retry-After” header
"""
write_api_batch = client.write_api(write_options=WriteOptions(batch_size=500, flush_interval=10_000, jitter_interval=2_000, retry_interval=5_000))


# with InfluxDBClient(url=url, token=token, org=org) as client:
#     p = Point("weatherstation") \
#         .tag("location", "San Francisco") \
#         .field("temperature", 25.9) \
#         .time(datetime.utcnow(), WritePrecision.MS)
#
#     with client.write_api(write_options=SYNCHRONOUS) as write_api:
#         write_api.write(bucket=bucket, record=p)
