#!/usr/bin/python3
"""
lists first State objects from the database hbtn_0e_6_usa

Args:
    mysql username
    mysql password
    mysql database name
"""
import sys
from sqlalchemy import (create_engine)
from model_state import Base, State
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

    res = session.query(State).first()

    if res:
        print("{}: {}".format(res.id, res.name))
    else:
        print("Nothing")
