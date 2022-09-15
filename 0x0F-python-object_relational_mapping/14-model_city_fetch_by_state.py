#!/usr/bin/python3
"""
prints all City objects from the db

Args:
    mysql username
    mysql password
    mysql database name
"""
import sys
from sqlalchemy import (create_engine)
from model_state import Base, State
from model_city import City
from sqlalchemy.engine.url import URL
from sqlalchemy.orm.session import Session


if __name__ == "__main__":
    mysql_u = sys.argv[1]
    mysql_p = sys.argv[2]
    mysql_db = sys.argv[3]
    mysql_h = "localhost"

    url = {'drivername': 'mysql+mysqldb', 'host': mysql_h,
           'username': mysql_u, 'password': mysql_p, 'database': mysql_db}
    engine = create_engine(URL(**url), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(bind=engine)

    res = session.query(City, State).filter(City.state_id == State.id)

    for city, state in res:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
