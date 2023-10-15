from typing import Optional
from uuid import UUID
from pydantic import BaseModel
from beanie import Document


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenPayload(BaseModel):
    uuid: Optional[UUID] = None