import os
from dotenv import load_dotenv
from influxdb_client import InfluxDBClient, Point, WriteOptions

INFLUX_TOKEN = os.getenv('INFLUX_TOKEN')
INFLUX_ORG = os.getenv('INFLUX_ORG')
INFLUX_BUCKET = os.getenv('INFLUX_BUCKET')
INFLUX_URL = os.getenv('INFLUX_URL')
load_dotenv()

url = INFLUX_URL
token = INFLUX_TOKEN
org = INFLUX_ORG
bucket = INFLUX_BUCKET

query = 'from(bucket: "my-bucket")|> range(start: -10m)|> filter(fn: (r) => r._measurement == "h2o_feet")|> filter(' \
        'fn: (r) => r._field == "water_level")|> filter(fn: (r) => r.location == "coyote_creek") '

# establish a connection
client = InfluxDBClient(url="http://localhost:9999", token=token, org=org)

# instantiate the WriteAPI and QueryAPI
write_api = client.write_api()
query_api = client.query_api()

# create and write the point
p = Point("h2o_feet").tag("location", "coyote_creek").field("water_level", 1)
write_api.write(bucket=bucket, org=org, record=p)

# return the table and print the result
result = client.query_api().query(org=org, query=query)
results = []
for table in result:
    for record in table.records:
        results.append((record.get_value(), record.get_field()))
print(results)
