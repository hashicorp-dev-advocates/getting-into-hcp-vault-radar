import os

import boto3
import psycopg2
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


def slack():
    url = "https://slack.com/api/chat.postMessage"
    headers = {"Authorization": "Bearer xoxb-0843-5678-91011"}
    data = {"channel": "#general", "text": "Hello, Slack!"}

    response = requests.post(url, headers=headers, json=data)
    print(response.status_code)
    print(response.text)


def apiv2():
    url = "https://api.michaelkosir.com/"

    username = "mkosir"
    password = "bG@abW7[76NJ$9QeR$x5"
    auth = (username, password)

    response = requests.get(url, auth=auth)
    print(response.status_code)
    print(response.text)


def db():
    conn = psycopg2.connect(
        dbname="postgres",
        user="webapp0001",
        password="y69C2s6r97Y5uUx",
        host="postgres.db.svc.cluster.local",
    )
    cur = conn.cursor()
    cur.execute("SELECT version();")
    print(cur.fetchone())
    cur.close()
    conn.close()


if __name__ == "__main__":
    aws()
    api()
    slack()
    db()
    apiv2()
