from sqlalchemy import Column, String, Text

from app.core.constants import MAX_NAME_LENGTH
from app.models.base import CharityProjectDonationGeneric

from ..core.db import Base


class CharityProject(Base, CharityProjectDonationGeneric):
    name = Column(String(MAX_NAME_LENGTH), unique=True, nullable=False)
    description = Column(Text, nullable=False)
