#!/usr/bin/python3
"""
Select states module from database hbtn_0e_0_usa script

Args:
    mysql username
    mysql password
    mysql database name
"""

import sys
import MySQLdb

if__name__ = "__main__":
    mysql_u = sys.argv[1]
    mysql_p = sys.argv[2]
    mysql_db = sys.argv[3]

    db = MySQLdb.connect(user=mysql_u, passwd=mysql_p, db=mysql_db)
    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY id")
    rows = cur.fetchall()

    for row in rows:
        print(row)
