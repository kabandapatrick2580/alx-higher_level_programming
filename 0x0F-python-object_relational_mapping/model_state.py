#!/usr/bin/python3
"""
script defining a state  class and  an instance base
"""

from sqlalchemy import Column
from sqlalchemy import Table
from sqlalchemy.orm import declarative_base
from sqlalchemy import Integer, String
Base = declarative_base()

class State (Base):
        """
        state class 
        """
        __tablename__ = 'states'

        id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
        name = Column(String(128), nullable=False)
