#!/usr/bin/python3
"""
Filter states module from database hbtn_0e_0_usa script

Args:
    mysql username
    mysql password
    mysql database name
"""

import sys
import MySQLdb

if __name__ == "__main__":
    mysql_u = sys.argv[1]
    mysql_p = sys.argv[2]
    mysql_db = sys.argv[3]

    db = MySQLdb.connect(user=mysql_u, passwd=mysql_p, db=mysql_db)
    cur = db.cursor()

    cur.execute("SELECT cities.id, cities.name, states.name \
        FROM cities, states WHERE cities.state_id = states.id \
            ORDER BY cities.id")
    rows = cur.fetchall()

    for row in rows:
        print(row)
