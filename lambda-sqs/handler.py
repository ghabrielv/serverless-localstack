import boto3
import os

client = boto3.client("sqs")


def enqueue(event, context):
    message = event["body"]

    print(f'Sending message to SQS: {os.environ.get("QUEUE_URL")}')

    client.send_message(QueueUrl=os.environ.get("QUEUE_URL"), MessageBody=message)

    response = "Enqueue OK!"

    return {"statusCode": 200, "body": response}
