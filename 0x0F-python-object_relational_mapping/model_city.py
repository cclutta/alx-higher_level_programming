#!/usr/bin/python3
"""Model city module """

from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.schema import ForeignKey
from model_state import Base


class City(Base):
    """City class

        Attributes:
        id: id of the state
        name: name of the state
        state_id: id of the state of the city
    """
    __tablename__ = "cities"

    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
