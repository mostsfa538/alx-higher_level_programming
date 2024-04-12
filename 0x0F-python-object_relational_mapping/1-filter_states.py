#!/usr/bin/python3
"""Here goes every thing"""
import MySQLdb
import sys


def filter_states(username, password, database):
    """lists all states with a name starting with N"""

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)
    cursor = db.cursor()

    cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY\
        'N%' ORDER BY states.id ASC")
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()


if __name__ == '__main__':
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    filter_states(username, password, database)
