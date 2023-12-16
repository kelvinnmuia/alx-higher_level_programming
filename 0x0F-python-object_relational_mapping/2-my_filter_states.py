#!/usr/bin/python3
"""
lists all states from the database in ascending order
using MySQLdb
"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    dbcon = MySQLdb.connect(host="localhost", user=argv[1],
                            passwd=argv[2], db=argv[3])
    curs = dbcon.cursor()
    curs.execute("""SELECT id, name FROM states WHERE name LIKE BINARY '{}'
                 ORDER BY states.id ASC""".format(argv[4]))
    rows = curs.fetchall()
    for row in rows:
        print(row)
    curs.close()
    dbcon.close()
