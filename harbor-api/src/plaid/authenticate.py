import os
from dotenv import load_dotenv
from plaid.api import plaid_api
from plaid.configuration import Configuration
from plaid.model.link_token_create_request_user import LinkTokenCreateRequestUser
from plaid.model.products import Products
from plaid.model.country_code import CountryCode
from plaid.model.link_token_create_request import LinkTokenCreateRequest
from plaid.model.item_public_token_exchange_request import ItemPublicTokenExchangeRequest
from plaid import ApiClient

load_dotenv()

PLAID_CLIENT_ID = os.getenv("PLAID_CLIENT_ID")
PLAID_SECRET = os.getenv("PLAID_SECRET")
PLAID_ENV = os.getenv("PLAID_ENV", "sandbox")

# Environment base URL
PLAID_BASE_URLS = {
    "sandbox": "https://sandbox.plaid.com",
    "development": "https://development.plaid.com",
    "production": "https://production.plaid.com"
}

configuration = Configuration(
    host=PLAID_BASE_URLS[PLAID_ENV],
    api_key={
        "clientId": PLAID_CLIENT_ID,
        "secret": PLAID_SECRET,
    }
)

api_client = ApiClient(configuration)
client = plaid_api.PlaidApi(api_client)