#!/usr/bin/python3
"""Here goes every thing"""
import MySQLdb
import sys


def my_filter_states(username, password, database, name):
    """
        takes in an argument and displays all values in the states table of
        hbtn_0e_0_usa where name matches the argument
    """

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)
    cursor = db.cursor()

    cursor.execute(
        "SELECT * FROM states WHERE name = '{}' \
        ORDER BY states.id ASC".format(name))
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()


if __name__ == '__main__':
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    name = sys.argv[4]
    my_filter_states(username, password, database, name)
