import os

import boto3
import requests

sts_client = boto3.client(
    service_name="sts",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name="us-east-2",
)

WEATHER_API = "A8F3F608-6BF2-49EE-9A25-DA4E9B394813"

DB_USER = "app001"
DB_PWD = "CDA92C26-B8E7-4A33-8336-671E52BF8C35"

def aws():
    response = sts_client.get_caller_identity()
    print(response)


def api():
    url = "https://michaelkosir.com/api/endpoint"
    headers = {"Authorization": "mk-123-74632"}

    response = requests.get(url, headers=headers)
    print(response.status_code)
    print(response.text)


def slack():
    url = "https://slack.com/api/chat.postMessage"
    headers = {"Authorization": "Bearer xoxb-0843-5678-91011"}
    data = {"channel": "#general", "text": "Hello, Slack!"}

    response = requests.post(url, headers=headers, json=data)
    print(response.status_code)
    print(response.text)


if __name__ == "__main__":
    aws()
    api()
    slack()
