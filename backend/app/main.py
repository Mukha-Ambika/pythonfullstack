
"""
This module contains the main FastAPI application for the Sharbo API.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum
import uvicorn

from app.routers import auth

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000","http://localhost:3000/","*"],  
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],  # Add more methods as needed
    allow_headers=["*"],  # Allow all headers
)

# Lambda handler
handler = Mangum(app)

app.include_router(auth.router)

@app.get("/")
async def read_root():
    """
    Root endpoint of the API.
    Returns a welcome message.
    """
    return {"message": "Welcome to Sharbo! This is the root endpoint"}


@app.get("/scrape")
async def read_root2():
    """
    Endpoint for scraping data.
    Returns a welcome message for scraping.
    """
    return {"message": "Welcome to Sharbo!2"}


# This allows the handler to work as expected when run locally
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
