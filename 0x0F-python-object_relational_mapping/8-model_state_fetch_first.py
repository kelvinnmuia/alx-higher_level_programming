#!/usr/bin/python3
"""
prints the first State object in the state database using SQLAlchemy
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
    ins = session.query(State).first()
    if ins is not None:
        print("{}: {}".format(ins.id, ins.name))
    else:
        print("Nothing")
    session.close()
