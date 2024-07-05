"""
Routes for handling authentication.
"""

from fastapi import APIRouter
from app.utils.security import *
from app.schemas.auth import *


router = APIRouter()


@router.post("/login/")
def login_route(user: Login):
    """
    Handle the login route.

    Args:
        user (Login): The user object containing email address and password.

    Returns:
        Response: The response from the login request.
    """
    clerk_login_url = f"{CLERK_API_FRONTEND_URL}/v1/client/sign_ins"
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
    """
    Register a user using the provided user information.

    Args:
        user (Register): The user information for registration.

    Returns:
        dict: The response from the registration API.

    Raises:
        Exception: If there is an error during the registration process.
    """
    
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


@router.post("/logout/")
def logout_route(user: Logout):
    """
    Handle the logout route.

    Returns:
        Response: The response from the logout request.
    """
    clerk_logout_url = f"{CLERK_API_FRONTEND_URL }/v1/client/sessions/{user.session_id}/end"
    print(clerk_logout_url)
    headers = BASE_HEADERS.copy()
    return make_request(clerk_logout_url, headers, "post", data=None)
  
