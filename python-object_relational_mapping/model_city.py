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

    # Comment out the following line for other tasks to avoid conflicts.
    state = relationship("State", back_populates="cities")

# the above code works for the tasks before the task 14
#remember to change it from test to code

"""
This module defines the City class.
"""
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base

class City(Base):
    
   # City class that represents the cities table.

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
"""
