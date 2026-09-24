import boto3
from botocore.exceptions import ClientError,BotoCoreError
import logging
import json

logger = logging.getLogger(__name__)



class S3Persistance:
    def __init__(self,bucket_name): 
        self.bucket_name = bucket_name
        self.s3_client = boto3.client("s3")
        
    def upload_file(self, data: dict, destination_key: str) -> None:
        try:
            self.s3_client.put_object(
                Bucket=self.bucket_name,
                Key=destination_key,
                Body=data,
                ContentType="application/json")
            logger.info(f"File {destination_key} uploaded to {self.bucket_name}")
        except (BotoCoreError, ClientError) as e:
            logger.error(f"Failed to upload {destination_key} to S3: {e}")
            raise

