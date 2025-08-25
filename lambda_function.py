import json
import boto3
import logging
from datetime import datetime

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    current_data = datetime.now().strftime("%Y-%m-%d")

    try:
        response = ec2.create_snapshot(
        VolumeId = 'vol-xxxxxxxxxxxxxxxxx',
        Description = 'My ec2 snapshot',
        TagSpecifications = [
            {
                 'ResourceType': 'snapshot',
                 'Tags': [
                    {
                        'Key': 'Name',
                        'Value': f"my EC2 snapshot{current_data}"
                    }


                ]

                }
            ]
        )
        logger.info(f"EC2 has been created successfully: {json.dumps(response, default=str)}")



    except Exception as e:
        logger.error(f"Your EC2 snapshot creation failed: {e}")
