import logging
import os

import boto3
from botocore.exceptions import ClientError
from rich.pretty import pprint


def upload_file_to_s3(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """
    if object_name is None:
        object_name = os.path.basename(file_name)

    s3_client = boto3.client("s3")
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
        pprint(f"File {file_name} uploaded to s3 successfully")
    except ClientError as e:
        logging.error(e)
        return False
    return True
