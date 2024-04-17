import random
import requests


def printable(event, context):

    id = random.randint(1, 100)

    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{id}").json()

    print(response["title"])

    return {"statusCode": 200, "body": "OK"}
