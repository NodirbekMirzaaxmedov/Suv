from datetime import date
from pydantic import BaseModel, validator
from sqlalchemy import *

class CreateContract(BaseModel):
    name: str
    customer_loc_id: int
    quantity: int
    deadline: date
    
    class Config:
        arbitrary_types_allowed = True

    @validator('deadline', pre=True)
    def parse_date(cls, value):
            if isinstance(value, str):
                return date.fromisoformat(value)
            return value

class UpdateContract(BaseModel):
    id: int
    quantity: int
    deadline: date
    status: str

    class Config:
        arbitrary_types_allowed = True

    @validator('deadline', pre=True)
    def parse_date(cls, value):
            if isinstance(value, str):
                return date.fromisoformat(value)
            return value