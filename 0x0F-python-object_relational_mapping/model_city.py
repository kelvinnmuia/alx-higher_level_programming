#!/usr/bin/python3
"""
defines the City class which inherits from Base = declarative_base()
and uses SQLAlchemy to link to MySQL table cities
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """
    defines the City class which links to the table cities
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
