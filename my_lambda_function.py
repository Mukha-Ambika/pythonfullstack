from fastapi import FastAPI, HTTPException
import requests
from bs4 import BeautifulSoup
import pandas as pd
from mangum import Mangum

from app.utils.get_env import *

app = FastAPI()
# Lambda handler
handler = Mangum(app)

@app.get("/scrape")
def scrape_wikipedia():
    try:
        return {
            'statusCode': 200,
            'body': CLERK_API_BASE_URL
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

