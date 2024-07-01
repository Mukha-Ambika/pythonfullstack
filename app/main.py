
"""
This module contains the main FastAPI application for the Sharbo API.
"""

from fastapi import FastAPI
from mangum import Mangum
import uvicorn

from app.routers import auth

app = FastAPI()
# Lambda handler
handler = Mangum(app)

app.include_router(auth.router)

@app.get("/")
async def read_root():
    """
    Root endpoint of the API.
    Returns a welcome message.
    """
    return {"message": "Welcome to Sharbo!"}


@app.get("/scrape")
async def read_root2():
    """
    Endpoint for scraping data.
    Returns a welcome message for scraping.
    """
    return {"message": "Welcome to Sharbo!2"}


# This allows the handler to work as expected when run locally
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)
