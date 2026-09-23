import json
import boto3
import os

sns = boto3.client('sns')
dynamodb = boto3.resource('dynamodb')

TOPIC_ARN = os.environ.get("TOPIC_ARN")
TABLE_NAME = os.environ.get("TABLE_NAME")

table = dynamodb.Table(TABLE_NAME)

def lambda_handler(event, context):

    print("===================================")
    print("Lambda execution started")
    print(json.dumps(event, indent=2))
    print("===================================")

    try:

        if "Records" not in event:
            print("No Records found in event")
            return {
                "statusCode": 400,
                "body": json.dumps("Invalid event format")
            }

        record = event["Records"][0]

        bucket_name = record["s3"]["bucket"]["name"]
        object_key = record["s3"]["object"]["key"]

        print(f"Bucket Name: {bucket_name}")
        print(f"Object Key: {object_key}")

        # Process only txt files
        if not object_key.endswith(".txt"):
            print(f"Skipping non-text file: {object_key}")

            return {
                "statusCode": 200,
                "body": json.dumps("File skipped")
            }

        # Store metadata in DynamoDB
        table.put_item(
            Item={
                "object_key": object_key,
                "bucket_name": bucket_name
            }
        )

        print("DynamoDB update successful")

        # Send SNS notification
        sns.publish(
            TopicArn=TOPIC_ARN,
            Subject="S3 Event Notification",
            Message=(
                f"S3 file processed successfully\n\n"
                f"Bucket: {bucket_name}\n"
                f"Object: {object_key}"
            )
        )

        print("SNS notification sent successfully")
        print("Lambda execution completed successfully")

        return {
            "statusCode": 200,
            "body": json.dumps(
                f"Successfully processed {object_key}"
            )
        }

    except Exception as e:

        print("===================================")
        print("Lambda execution failed")
        print(str(e))
        print("===================================")

        raise
