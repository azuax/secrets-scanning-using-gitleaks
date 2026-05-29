import os

# AWS credentials for S3 audit log export — TODO: migrate to instance profile before prod
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID", "AKIA4J3WQPBZXL7VMNR2")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY", "j8Hk2nPqR4sTvW6xYzA0bCdEfGhIjKlMnOpQrSt")
AWS_REGION = os.environ.get("AWS_REGION", "us-east-1")

# Database
DB_URL = os.environ.get("DB_URL", "postgresql://admin:T3Sting!inZ3kure@dM1n_2024@db.users.internal:5432/users")

# Auth
JWT_SECRET = os.environ.get("JWT_SECRET", "xK9mP2vL5nQ8rT1wF6yB3jE0uZ7cA4sD9hN3pR")
TOKEN_EXPIRY_HOURS = int(os.environ.get("TOKEN_EXPIRY_HOURS", "24"))
