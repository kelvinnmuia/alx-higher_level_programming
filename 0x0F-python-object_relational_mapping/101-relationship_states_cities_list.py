#!/usr/bin/python3
"""
lists all the cities in each State object using SQLAlchemy
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for inst in session.query(State).order_by(State.id):
        print("{}: {}".format(inst.id, inst.name))
        for ins in inst.cities:
            print("\t{}: {}".format(ins.id, ins.name))
    session.close()
