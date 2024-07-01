from fastapi import FastAPI
from app.routers import auth
from mangum import Mangum

app = FastAPI()
# Lambda handler
handler = Mangum(app)

app.include_router(auth.router)

@app.get("/")
async def read_root():
    return {"message": "Welcome to Sharbo!"}


@app.get("/scrape")
async def read_root2():
    return {"message": "Welcome to Sharbo!2"}



# This allows the handler to work as expected when run locally
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=80)
