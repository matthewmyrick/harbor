from fastapi import FastAPI, HTTPException
from src.plaid.authenticate import client
from plaid.model.link_token_create_request import LinkTokenCreateRequest
from plaid.model.products import Products
from plaid.model.country_code import CountryCode
from plaid.model.item_public_token_exchange_request import ItemPublicTokenExchangeRequest

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Plaid FastAPI is running!"}

@app.get("/create_link_token")
def create_link_token():
    request = LinkTokenCreateRequest(
        products=[Products("transactions")],
        client_name="My App",
        country_codes=[CountryCode("US")],
        language="en",
        user={"client_user_id": "unique-user-id"}
    )

    response = client.link_token_create(request).execute()
    return response.to_dict()

@app.post("/exchange_public_token")
def exchange_public_token(public_token: str):
    try:
        request = ItemPublicTokenExchangeRequest(public_token=public_token)
        response = client.item_public_token_exchange(request).execute()
        access_token = response['access_token']
        item_id = response['item_id']
        return {"access_token": access_token, "item_id": item_id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))