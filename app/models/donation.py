from sqlalchemy import Column, ForeignKey, Integer, Text

from app.core.db import Base
from app.models.base import CharityProjectDonationGeneric


class Donation(Base, CharityProjectDonationGeneric):
    user_id = Column(Integer, ForeignKey("user.id"))
    comment = Column(Text)
