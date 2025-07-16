import os
from plaid import Client
from dotenv import load_dotenv

load_dotenv()

PLAID_CLIENT_ID = os.getenv("PLAID_CLIENT_ID")
PLAID_SECRET = os.getenv("PLAID_SECRET")
PLAID_ENV = os.getenv("PLAID_ENV", "sandbox")

plaid_envs = {
    "sandbox": "sandbox",
    "development": "development",
    "production": "production"
}

client = Client(
    client_id=PLAID_CLIENT_ID,
    secret=PLAID_SECRET,
    environment=plaid_envs[PLAID_ENV],
)