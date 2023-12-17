#!/usr/bin/python3
"""
updates the name of the State whose id = 2 to 'New Mexico'
"""

from sys import argv
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for ins in session.query(State).filter_by(id=2):
        ins.name = 'New Mexico'
    session.commit()
    session.close()
