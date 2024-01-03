import os, time
from dotenv import load_dotenv
from influxdb_client_3 import InfluxDBClient3, Point

INFLUX_TOKEN = os.environ.get('INFLUX_TOKEN')
INFLUX_ORG = os.environ.get('INFLUX_ORG')
INFLUX_BUCKET = os.environ.get('INFLUX_BUCKET')
INFLUX_URL = os.environ.get('INFLUX_URL')
INFLUX_DBNAME = os.environ.get('INFLUX_DBNAME')

load_dotenv()

host = INFLUX_URL
token = INFLUX_TOKEN
org = INFLUX_ORG
bucket = INFLUX_BUCKET
database = INFLUX_DBNAME

# establish a connection
client = InfluxDBClient3(host=host, token=token, org=org)

data = {
  "point1": {
    "location": "Klamath",
    "species": "bees",
    "count": 23,
  },
  "point2": {
    "location": "Portland",
    "species": "ants",
    "count": 30,
  },
  "point3": {
    "location": "Klamath",
    "species": "bees",
    "count": 28,
  },
  "point4": {
    "location": "Portland",
    "species": "ants",
    "count": 32,
  },
  "point5": {
    "location": "Klamath",
    "species": "bees",
    "count": 29,
  },
  "point6": {
    "location": "Portland",
    "species": "ants",
    "count": 40,
  },
}

for key in data:
  point = (
    Point("census")
    .tag("location", data[key]["location"])
    .field(data[key]["species"], data[key]["count"])
  )
  client.write(database=database, record=point)
  time.sleep(1) # separate points by 1 second

print("Complete. Return to the InfluxDB UI.")
