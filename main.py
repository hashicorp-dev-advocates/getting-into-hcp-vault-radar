import os

import boto3

SESSION_KEY = "7rR>8(EN4Vp@35*VpA:0F=£2"

sts_client = boto3.client(
    service_name="sts",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name="us-east-2",
)


def aws():
    response = sts_client.get_caller_identity()
    print(response)


if __name__ == "__main__":
    aws()
