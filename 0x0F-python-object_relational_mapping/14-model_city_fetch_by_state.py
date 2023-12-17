#!/usr/bin/python3
"""
lists all the cities in ascending order by id using SQLAlchemy
"""

from sys import argv
from model_state import Base, State
from model_city import City

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for ins in session.query(City, State).join(
            State, City.state_id == State.id).order_by(City.id):
        print("{}: ({}) {}".format(
            ins[1].name, ins[0].id, ins[0].name))
    session.close()
