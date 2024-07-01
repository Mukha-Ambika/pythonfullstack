"""
This module provides functions to retrieve environment variables for the Sharbo API.

The module checks the value of the 'ENVIRONMENT' environment variable. If it is set to 'staging', the module uses environment variables directly. Otherwise, it loads the values from a .env file using the `dotenv` library.

The following environment variables are retrieved:
- CLERK_PUBLISHABLE_KEY: The publishable key for Clerk.
- CLERK_SECRET_KEY: The secret key for Clerk.
- CLERK_API_FRONTEND_URL: The frontend API URL for Clerk.
- CLERK_API_BASE_URL: The base API URL for Clerk.
- CLERK_TESTING_TOKEN: The testing token for Clerk.

Note: Make sure to set the 'ENVIRONMENT' environment variable accordingly before running this module.

"""

import os

if os.getenv('ENVIRONMENT') == "staging":
    # Use environment variables directly in staging
    CLERK_PUBLISHABLE_KEY = os.environ['CLERK_PUBLISHABLE_KEY']
    CLERK_SECRET_KEY = os.environ['CLERK_SECRET_KEY']
    CLERK_API_FRONTEND_URL = os.environ['CLERK_FRONTEND_API_URL']
    CLERK_API_BASE_URL = os.environ['CLERK_API_URL']
    CLERK_TESTING_TOKEN = os.environ['CLERK_TESTING_TOKEN']
else:
    from dotenv import dotenv_values

    # Load the .env file
    env_values = dotenv_values('.env')

    # Get the values
    CLERK_PUBLISHABLE_KEY = env_values['CLERK_PUBLISHABLE_KEY']
    CLERK_SECRET_KEY = env_values['CLERK_SECRET_KEY']
    CLERK_API_FRONTEND_URL = env_values['CLERK_FRONTEND_API_URL']
    CLERK_API_BASE_URL = env_values['CLERK_API_URL']
    CLERK_TESTING_TOKEN = env_values['CLERK_TESTING_TOKEN']
