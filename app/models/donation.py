from sqlalchemy import Column, ForeignKey, Integer, Text

from app.models.base import CharityProjectDonationGeneric


class Donation(CharityProjectDonationGeneric):
    user_id = Column(Integer, ForeignKey("user.id"))
    comment = Column(Text)
