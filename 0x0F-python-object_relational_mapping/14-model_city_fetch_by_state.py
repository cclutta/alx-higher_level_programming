#!/usr/bin/python3
"""
Script that prints all `City` objects from the db

Arguments:
    mysql username (str)
    mysql password (str)
    database name (str)
"""

import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
from sqlalchemy.engine.url import URL
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    mysql_u = sys.argv[1]
    mysql_p = sys.argv[2]
    mysql_db = sys.argv[3]

    url = {'drivername': 'mysql+mysqldb', 'host': 'localhost',
           'username': mysql_u, 'password': mysql_p, 'database': mysql_db}

    engine = create_engine(URL(**url), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(bind=engine)

    res = session.query(City, State)
    print(res)
