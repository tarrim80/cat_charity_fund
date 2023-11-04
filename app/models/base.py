from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Integer


class CharityProjectDonationGeneric:
    full_amount = Column(Integer)
    invested_amount = Column(Integer)
    fully_invested = Column(Boolean, default=False)
    create_date = Column(DateTime, default=datetime.now)
    close_date = Column(DateTime)
