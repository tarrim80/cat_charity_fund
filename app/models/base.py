from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Integer
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import validates

from app.core.constants import MIN_AMOUNT, ErrorMsg
from app.core.db import Base


class CharityProjectDonationGeneric(Base):
    __abstract__ = True

    full_amount = Column(Integer)
    invested_amount = Column(Integer, default=0)
    fully_invested = Column(Boolean, default=False)
    create_date = Column(DateTime, default=datetime.now)
    close_date = Column(DateTime)

    @hybrid_property
    def missing_amount(self) -> int:
        return self.full_amount - self.invested_amount

    @validates("full_amount")
    def validate_full_amount(self, key, value):
        if value < MIN_AMOUNT:
            raise ValueError(ErrorMsg.MUST_GREATER_THAN_ZERO)
        return value
