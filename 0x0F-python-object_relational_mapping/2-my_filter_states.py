#!/usr/bin/python3
""" script that takes in an argument and displays all values in the states
    table of hbtn_0e_0_usa where name matches the argument
    Usage: ./2-my_filter_states.py <mysql username>
                                    <mysql password>
                                    <database name>
                                    <state name searched>
"""
from sys import argv
import MySQLdb as db


if __name__ == "__main__":
    """
    Access to the database and get the states
    from the database.
    """
    db_connect = db.connect(host="localhost", port=3301, user=argv[1],
                            passwd=argv[2], db=argv[3])
    db_cursor = db_connect.cursor()
    db_cursor.execute("SELECT * FROM states \
                        WHERE name LIKE BINARY '{}' \
                        ORDER BY states.id ASC".format(argv[4]))
    rows = db_cursor.fetchall()
    for row in rows:
        print(row)
