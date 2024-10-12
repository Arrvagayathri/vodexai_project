from pydantic import BaseModel, EmailStr
from datetime import date, datetime
from typing import Optional

class Item(BaseModel):
    name: str
    email: EmailStr
    item_name: str
    quantity: int
    expiry_date: date

class UpdateItem(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
    item_name: Optional[str]
    quantity: Optional[int]
    expiry_date: Optional[date]

class ClockIn(BaseModel):
    email: EmailStr
    location: str

class UpdateClockIn(BaseModel):
    email: Optional[EmailStr]
    location: Optional[str]
