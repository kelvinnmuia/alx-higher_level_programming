#!/usr/bin/python3
"""
defines the State class which inherits from Base = declarative_base()
and links to MySQL table states using SQLAlchemy
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """
    defines State class that links to MySQL table 'state'
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete", backref="state")
