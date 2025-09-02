import os

import boto3
import requests

sts_client = boto3.client(
    service_name="sts",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name="us-east-2",
)


def aws():
    response = sts_client.get_caller_identity()
    print(response)


def api():
    url = "https://michaelkosir.com/api/endpoint"
    headers = {"Authorization": "mk-123-74632"}

    response = requests.get(url, headers=headers)
    print(response.status_code)
    print(response.text)


if __name__ == "__main__":
    aws()
    api()
