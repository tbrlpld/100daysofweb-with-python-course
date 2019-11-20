import sqlalchemy as sa

from .base import Base


class Scooter(Base):
    __tablename__ = "scooters"
    id = sa.Column(sa.Integer, primary_key=True)
