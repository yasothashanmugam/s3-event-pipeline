import json

def lambda_handler(event, context):
    try:
        print("S3 Event Received")

        print("Event:")
        print(json.dumps(event, indent=2))

        if event.get("source") == "aws.s3":
            detail = event.get("detail", {})

            bucket_name = detail.get("bucket", {}).get("name")
            object_key = detail.get("object", {}).get("key")

            print(f"Bucket Name: {bucket_name}")
            print(f"Object Key: {object_key}")

        return {
            "statusCode": 200,
            "body": json.dumps("S3 event processed successfully")
        }

    except Exception as e:
        print(f"Error occurred: {str(e)}")

        return {
            "statusCode": 500,
            "body": json.dumps(f"Error: {str(e)}")
        }