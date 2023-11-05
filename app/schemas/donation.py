from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, conint


class DonationBase(BaseModel):
    full_amount: conint(gt=0)
    comment: Optional[str] = None


class DonationCreate(DonationBase):
    pass


class DonationDB(DonationCreate):
    id: int
    create_date: datetime
    user_id: UUID
    invested_amount: int
    fully_invested: bool
    close_date: Optional[datetime]

    class Config:
        orm_mode = True
