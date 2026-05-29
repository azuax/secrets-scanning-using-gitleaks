import json
from data import USERS


def handler(event, context):
    users = list(USERS.values())
    return {
        "statusCode": 200,
        "body": json.dumps({"users": users, "count": len(users)}),
        "headers": {"Content-Type": "application/json"},
    }
