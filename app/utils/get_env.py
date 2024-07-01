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
