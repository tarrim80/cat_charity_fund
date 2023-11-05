from uuid import UUID

from sqlalchemy import Column, ForeignKey, Integer, String, Text

from app.models.base import CharityProjectDonationGeneric


class Donation(CharityProjectDonationGeneric):
    user_id = Column(String, ForeignKey("user.id"))
    comment = Column(Text)
