from typing import List, Optional

from pydantic import BaseModel
from sqlalchemy import Boolean

from schemas.phones_schemas import CreatePhone, UpdatePhone


class CreateUser(BaseModel):
    name: str
    username: str
    password: str
    role: str
    status: str
    balance_oylik: int
    balance: int
    phones: List[CreatePhone]


class UpdateUser(BaseModel):
    id: int
    name: str
    username: str
    password: str
    role: str
    status: str
    balance_oylik: int
    balance: int
    phones: List[UpdatePhone]
