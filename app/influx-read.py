from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('path/to/.env')
load_dotenv(dotenv_path=dotenv_path)
from influxdb_client import InfluxDBClient

url = 'https://us-west-2-1.aws.cloud2.influxdata.com'
token = 'my-token'
org = 'my-org'
bucket = 'my-bucket'

with InfluxDBClient(url=url, token=token, org=org) as client:
    query_api = client.query_api()

    tables = query_api.query('from(bucket: "my-bucket") |> range(start: -1d)')

    for table in tables:
        for record in table.records:
            print(str(record["_time"]) + " - " + record.get_measurement()
                  + " " + record.get_field() + "=" + str(record.get_value()))
