#!/usr/bin/python3
"""
List the contents of a database table.
"""

import MySQLdb as sql
from sys import argv


def main():
    """Main function."""
    my_host = "localhost"
    port = 3306
    my_user = argv[1]
    my_password = argv[2]
    d_base = argv[3]

    db = sql.connect(host=my_host, port=port, user=my_user,
                     passwd=my_password, db=d_base)
    cur = db.cursor()

    cur.execute("""
                SELECT cities.id, cities.name, states.name
                FROM cities JOIN states on cities.state_id = states.id
                ORDER BY cities.id
                """
                )

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
