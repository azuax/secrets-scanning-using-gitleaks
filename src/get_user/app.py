import json
from data import USERS


def handler(event, context):
    user_id = event.get("pathParameters", {}).get("user_id")
    user = USERS.get(user_id)
    if not user:
        return {
            "statusCode": 404,
            "body": json.dumps({"error": "User not found"}),
            "headers": {"Content-Type": "application/json"},
        }
    return {
        "statusCode": 200,
        "body": json.dumps(user),
        "headers": {"Content-Type": "application/json"},
    }
