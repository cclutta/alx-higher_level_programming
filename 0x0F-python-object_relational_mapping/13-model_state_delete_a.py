#!/usr/bin/python3
"""
deletes State objects with letter a

Args:
    mysql username
    mysql password
    mysql database name
"""
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
from sqlalchemy.engine.url import URL
from model_state import Base, State


if __name__ == "__main__":
    mysql_u = sys.argv[1]
    mysql_p = sys.argv[2]
    mysql_db = sys.argv[3]

    url = {'drivername': 'mysql+mysqldb', 'host': 'localhost',
           'username': mysql_u, 'password':  mysql_p, 'database':  mysql_db}

    engine = create_engine(URL(**url), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(bind=engine)

    res = session.query(State).filter(State.name.like('%a%')).order_by(State.id)
    for i in res:
        session.delete(i)

    session.commit()
