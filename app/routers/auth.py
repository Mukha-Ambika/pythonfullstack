from fastapi import APIRouter
from app.utils.security import *
from app.schemas.auth import *


router = APIRouter()


@router.post("/login/")
def login_route(user: Login):
    clerk_login_url = f"{CLERK_API_FRONTEND_URL }/v1/client/sign_ins"
    print(clerk_login_url)
    payload = {
        "strategy": "password",
        "identifier": user.email_address,
        "password": user.password

    }
    headers = BASE_HEADERS.copy()
    headers["Content-Type"] = "application/x-www-form-urlencoded"
    return make_request(clerk_login_url, headers, "post", data=payload)


@router.post("/register/")
def register_route(user: Register):
    clerk_register_url = f"{CLERK_API_FRONTEND_URL }/v1/client/sign_ups"
    payload = {
        "strategy": "email_code",
        # "first_name": user.first_name,
        # "last_name": user.last_name,
        "email_address": user.email_address,
        "password": user.password
    }

    params = {
        '__clerk_testing_token': CLERK_TESTING_TOKEN
    }
    
    headers = BASE_HEADERS.copy()
    headers["Content-Type"] = "application/x-www-form-urlencoded"

    create_signup_object = make_request(clerk_register_url, BASE_HEADERS, "post", params=params, data=payload)

    if create_signup_object.get('error'):
        return create_signup_object
    
    signup_id = create_signup_object['response']['id']

    clerk_first_verification_url = f"{CLERK_API_FRONTEND_URL }/v1/client/sign_ins/{signup_id}/prepare_first_factor"

    payload = {
        "strategy": "email_code",
        "email_address_id": user.email_address        
    }

    first_verification = make_request(f"{clerk_register_url}/{signup_id}/verify", BASE_HEADERS, "post")

    return first_verification