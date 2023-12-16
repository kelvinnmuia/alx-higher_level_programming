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
    curs.execute("""SELECT c.name FROM cities AS c \
                 INNER JOIN states AS s ON c.state_id = s.id \
                 WHERE s.name = '{}' \
                 ORDER BY c.id ASC""".format(argv[4]))
    rows = curs.fetchall()
    for i, row in enumerate(rows, start=0):
        if i != 0:
            print(", ", end="")
        print(row[0], end="")
    print("")
    curs.close()
    dbcon.close()
