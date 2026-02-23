import boto3
from botocore.exceptions import ClientError

secrets_client = boto3.client("secretsmanager")


def lambda_handler(event, context):
    secret_arn = event["SecretId"]
    token = event["ClientRequestToken"]
    step = event["Step"]

    metadata = secrets_client.describe_secret(SecretId=secret_arn)
    versions = metadata["VersionIdsToStages"]

    if token not in versions:
        raise ValueError("Secret version not found")

    if "AWSPENDING" not in versions[token]:
        raise ValueError("Secret version not staged for rotation")

    if step == "createSecret":
        create_secret(secret_arn, token)

    elif step == "finishSecret":
        finish_secret(secret_arn, token)


def create_secret(secret_arn, token):
    try:
        secrets_client.get_secret_value(
            SecretId=secret_arn,
            VersionId=token,
            VersionStage="AWSPENDING"
        )
        return
    except ClientError:
        pass

    current = secrets_client.get_secret_value(
        SecretId=secret_arn,
        VersionStage="AWSCURRENT"
    )

    if "SecretString" in current:
        secrets_client.put_secret_value(
            SecretId=secret_arn,
            ClientRequestToken=token,
            SecretString=current["SecretString"],
            VersionStages=["AWSPENDING"]
        )
    else:
        secrets_client.put_secret_value(
            SecretId=secret_arn,
            ClientRequestToken=token,
            SecretBinary=current["SecretBinary"],
            VersionStages=["AWSPENDING"]
        )


def finish_secret(secret_arn, token):
    metadata = secrets_client.describe_secret(SecretId=secret_arn)

    current_version = None
    for version, stages in metadata["VersionIdsToStages"].items():
        if "AWSCURRENT" in stages:
            current_version = version
            break

    if current_version == token:
        return

    secrets_client.update_secret_version_stage(
        SecretId=secret_arn,
        VersionStage="AWSCURRENT",
        MoveToVersionId=token,
        RemoveFromVersionId=current_version
    )
