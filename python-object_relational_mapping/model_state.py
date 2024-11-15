#!/usr/bin/python3
"""
This module defines a State class and a Base instance for SQLAlchemy.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """
    State class that represents the states table.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

    # This line should be uncommented for Task 14.
    cities = relationship("City", back_populates="state")

# For previous tasks, comment out the above relationship line and use the following:
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    # State class that represents the states table.
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

    # This line should be commented for Task 14.
    cities = relationship("City")
"""
