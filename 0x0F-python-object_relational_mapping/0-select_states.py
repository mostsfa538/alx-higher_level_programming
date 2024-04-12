#!/usr/bin/python3
"""Here goes every thing"""
import MySQLdb
import sys


def select_state(username, password, database):
    """lists all states from the database hbtn_0e_0_usa"""
    conn = MySQLdb.connect(host='localhost', port=3306,
                           user=username, password=password, db=database)
    cur = conn.cursor()

    cur.execute("SELECT * FROM states ORDER BY id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()


if __name__ == '__main__':
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    select_state(username, password, database)
