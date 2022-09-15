#!/usr/bin/python3
"""Model state module """

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """State class

        Attributes:
        id: id of the state
        name: name of the state
    """
    __tablename__ = "states"
    
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
