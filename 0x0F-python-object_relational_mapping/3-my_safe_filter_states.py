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
    state_name_searched = sys.argv[4]

    db = MySQLdb.connect(user=mysql_u, passwd=mysql_p, db=mysql_db)
    cur = db.cursor()
    
    q = "SELECT * FROM states WHERE name LIKE BINARY %s \
        ORDER BY id"

    cur.execute(q, (state_name_searched, ))
    rows = cur.fetchall()

    for row in rows:
        print(row)
