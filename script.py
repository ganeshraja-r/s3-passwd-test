import boto3
import json
import sys

bucket_name = "s3-config-pwd-test"
file_key = "config.json"

s3 = boto3.client("s3")
secrets = boto3.client("secretsmanager")

try:
    # STEP 1: Fetch config
    response = s3.get_object(Bucket=bucket_name, Key=file_key)
    config = json.loads(response["Body"].read())

    print("✅ Config file fetched from S3")

    # STEP 2: Extract ARN
    password_arn = config["tenants"]["TEST"]["db"]["password"]

    # STEP 3: Fetch secret
    secret_response = secrets.get_secret_value(SecretId=password_arn)
    real_password = secret_response["SecretString"]

    # ✅ REQUIRED MESSAGE
    print("✅ Password successfully fetched from Secrets Manager")

    if not real_password:
        print("❌ Password fetch failed. Stopping execution.")
        sys.exit(1)

    # STEP 4: Continue
    config["tenants"]["TEST"]["db"]["password"] = real_password

    print("➡️ Proceeding to next step...")
    print("✅ Config is ready to be used")

except Exception as e:
    print("❌ Error occurred:", str(e))
    sys.exit(1)