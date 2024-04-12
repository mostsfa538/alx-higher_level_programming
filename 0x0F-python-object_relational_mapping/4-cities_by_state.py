#!/usr/bin/python3
"""Here goes every thing"""
import MySQLdb
import sys


def cities_by_state(username, password, database):
    """
        takes in an argument and displays all values in the states table of
        hbtn_0e_0_usa where name matches the argument
    """

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)
    cursor = db.cursor()

    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities\
            INNER JOIN states ON states.id=cities.state_id")
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()


if __name__ == '__main__':
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    cities_by_state(username, password, database)
