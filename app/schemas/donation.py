from datetime import datetime
from typing import Optional

from pydantic import BaseModel, conint


class DonationBase(BaseModel):
    full_amount: conint(gt=0)
    comment: Optional[str] = None


class DonationCreate(DonationBase):
    pass


class DonationResponse(DonationCreate):
    id: int
    create_date: datetime

    class Config:
        orm_mode = True


class DonationDB(DonationResponse):
    user_id: int
    invested_amount: int
    fully_invested: bool
    close_date: Optional[datetime]
