#!/usr/bin/python3
"""Here goes every thing"""
import MySQLdb
import sys


def filter_cities(username, password, database, name):
    """
        takes in an argument and displays all values in the states table of
        hbtn_0e_0_usa where name matches the argument
    """

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)
    cursor = db.cursor()

    cursor.execute("SELECT cities.name FROM cities\
            INNER JOIN states ON states.id=cities.state_id WHERE states.name\
            LIKE BINARY '{}'".format(name))

    cities = cursor.fetchall()

    city_names = [city[0] for city in cities]
    formatted_cities = ", ".join(city_names)

    print(formatted_cities)
    cursor.close()
    db.close()


if __name__ == '__main__':
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    name = sys.argv[4]
    filter_cities(username, password, database, name)
