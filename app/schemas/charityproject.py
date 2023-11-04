from datetime import datetime
from typing import Annotated, Optional

from fastapi import HTTPException, status
from pydantic import BaseModel, Field, conint, validator

from app.core.constants import MAX_NAME_LENGTH, MIN_STRING_LENGTH


class CharityProjectBase(BaseModel):
    name: str = Field(
        ..., min_length=MIN_STRING_LENGTH, max_length=MAX_NAME_LENGTH
    )
    description: str = Field(..., min_length=MIN_STRING_LENGTH)
    full_amount: conint(gt=0)


class CharityProjectCreate(CharityProjectBase):
    pass


class CharityProjectDB(CharityProjectCreate):
    id: int
    invested_amount: int
    fully_invested: bool
    create_date: datetime
    close_date: Optional[datetime]

    class Config:
        orm_mode = True


class CharityProjectUpdate(CharityProjectBase):
    pass
