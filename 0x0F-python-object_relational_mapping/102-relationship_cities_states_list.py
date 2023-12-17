#!/usr/bin/python3
"""
lists all the City object and the corresponding
State object using SQLAlchemy
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
    for inst in session.query(City).order_by(City.id):
        print("{}: {}".format(inst.id, inst.name), end="")
        print(" -> {}".format(inst.state.name))
    session.close()
