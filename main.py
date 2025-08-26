import base64

import boto3
import hvac

AWS_ACCESS_KEY_ID = "AKIAE2647DD83A384175"
AWS_SECRET_ACCESS_KEY = "g4fEPvwN2+2kT8omL4ieFqgVj4xLWx40PxNmOJ3S"

VAULT_ADDR = "http://vault.example.com"
VAULT_TOKEN = "hvs.4kZkME6mRPIc9HGX3rpVet8p"

vault_client = hvac.Client(url=VAULT_ADDR, token=VAULT_TOKEN)

sts_client = boto3.client(
    service_name="sts",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name="us-east-2",
)


def aws():
    response = sts_client.get_caller_identity()
    print(response)


def kv():
    response = vault_client.secrets.kv.read_secret_version(path="path/to/my/secret")
    print(response)


def encrypt():
    # encrypt credit card number
    ccn = base64.b64encode(b"5105-1051-0510-5100").decode()
    response = vault_client.secrets.transit.encrypt_data(name="example", plaintext=ccn)
    print(response["data"]["ciphertext"])

    # encrypt social security number
    ssn = base64.b64encode(b"123-45-6789").decode()
    response = vault_client.secrets.transit.encrypt_data(name="example", plaintext=ssn)
    print(response["data"]["ciphertext"])


if __name__ == "__main__":
    aws()
    kv()
    encrypt()
