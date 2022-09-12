#!/usr/bin/python3
"""
Select states module

Args:
    mysql username
    mysql password
    mysql database name
"""

import sys
import MySQLdb

if__name__="__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    mysql_database = sys.argv[3]
    
    db = MySQLdb.connect(user=mysql_username, passwd=mysql_password, db=mysql_database)
    cur = db.cursor()
    
    cur.execute("SELECT * FROM states ORDER BY id")
    rows = cur.fetchall()

    for row in rows:
        print(row)

