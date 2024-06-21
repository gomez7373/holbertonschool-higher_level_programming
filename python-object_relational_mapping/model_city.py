#!/usr/bin/python3
"""
This module defines the City class.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base

class City(Base):
    """
    City class that represents the cities table.
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    # This line should be uncommented for Task 14.
    state = relationship("State", back_populates="cities")

# For previous tasks, comment out the above relationship line and use the following:
"""
# from sqlalchemy import Column, Integer, String, ForeignKey
# from model_state import Base

# class City(Base):
#     """
#     City class that represents the cities table.
#     """
#     __tablename__ = 'cities'

#     id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
#     name = Column(String(128), nullable=False)
#     state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
"""

