# app/schemas.py
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import date

class ContactCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str
    birth_date: date
    additional_info: Optional[str] = None

class ContactUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone_number: Optional[str] = None
    birth_date: Optional[date] = None
    additional_info: Optional[str] = None

class Contact(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str
    birth_date: date
    additional_info: Optional[str] = None

    class Config:
        orm_mode = True
