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

    # Comment out the following line for other tasks to avoid conflicts.
    cities = relationship("City", backref="state", cascade="all, delete-orphan")

"""
This module defines a State class and a Base instance for SQLAlchemy.
"""
'''
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class that represents the states table.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
'''
# the upper code works for the tasks before the task 14
#remember to change it from test to code 
