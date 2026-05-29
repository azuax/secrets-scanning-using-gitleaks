import json
from data import USERS


def handler(event, context):
    user_id = event.get("pathParameters", {}).get("user_id")
    if user_id not in USERS:
        return {
            "statusCode": 404,
            "body": json.dumps({"error": "User not found"}),
            "headers": {"Content-Type": "application/json"},
        }

    body = json.loads(event.get("body") or "{}")
    allowed_fields = {"name", "email", "role", "active"}
    updates = {k: v for k, v in body.items() if k in allowed_fields}

    if not updates:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "No valid fields to update"}),
            "headers": {"Content-Type": "application/json"},
        }

    USERS[user_id].update(updates)
    return {
        "statusCode": 200,
        "body": json.dumps(USERS[user_id]),
        "headers": {"Content-Type": "application/json"},
    }
