#!/usr/bin/python3
"""lsiting a database"""

import MySQLdb as sql
import sys


if __name__ == "__main__":
    """main function"""
    my_host = "localhost"
    port = 3306
    my_user = sys.argv[1]
    my_password = sys.argv[2]
    d_base = sys.argv[3]
    db = sql.connect(host=my_host, port=port, user=my_user,
                     passwd=my_password, db=d_base)
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
