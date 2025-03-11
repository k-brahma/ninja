import uuid
from typing import Optional

from pydantic import BaseModel, EmailStr


class LoginSchema(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: uuid.UUID
    email: str
    username: str


class TokenSchema(BaseModel):
    access_token: str
    token_type: str = "bearer"
