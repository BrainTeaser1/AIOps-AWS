import boto3

REGION = "us-east-1"

cloudwatch = boto3.client(
    "cloudwatch",
    region_name=REGION
)

logs = boto3.client(
    "logs",
    region_name=REGION
)

ec2 = boto3.client(
    "ec2",
    region_name=REGION
)
