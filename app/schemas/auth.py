from pydantic import BaseModel

class Login(BaseModel):
    email_address: str
    password: str

class Register(BaseModel):
    email_address: str
    password: str
    # first_name: str
    # last_name: str    