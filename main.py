import boto3

AWS_ACCESS_KEY_ID = "AKIAE2647DD83A384175"
AWS_SECRET_ACCESS_KEY = "g4fEPvwN2+2kT8omL4ieFqgVj4xLWx40PxNmOJ3S"

sts_client = boto3.client(
    service_name="sts",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name="us-east-2",
)


def aws():
    response = sts_client.get_caller_identity()
    print(response)


if __name__ == "__main__":
    aws()
