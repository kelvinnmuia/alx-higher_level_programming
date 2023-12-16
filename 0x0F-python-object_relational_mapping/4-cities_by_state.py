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
    curs.execute("""SELECT c.id, c.name, s.name FROM cities AS c \
                 INNER JOIN states AS s ON c.state_id = s.id \
                 ORDER BY c.id ASC""")
    rows = curs.fetchall()
    for row in rows:
        print(row)
    curs.close()
    dbcon.close()
