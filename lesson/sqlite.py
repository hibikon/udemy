"""How to use sqlite"""



"""Import Library"""

#import sqlite3


"""Create Database

    database name : first time

    :memory: : From the second time
"""

#conn = sqlite3.connect('test_sqlite.db')

#conn = sqlite3.connect(':memory:')


"""Cursor definition"""

#curs = conn.cursor()


"""Create Table

    table name : persons

    id : INTEGER

    name : STRING

    AUTOINCREMENT : Will automatically increase the id

    CREATE TABLE : only once
"""    

#curs.execute(
#    'CREATE TABLE persons(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)')
#conn.commit()


"""Add element"""

#curs.execute(
#    'INSERT INTO persons(name) values("Mike")'
#)
#conn.commit()


"""Element confirmation"""

#curs.execute('SELECT * FROM persons')
#curs.execute('INSERT INTO persons(name) values("Nancy")')
#curs.execute('INSERT INTO persons(name) values("Hibikon")')
#conn.commit()
#print(curs.fetchall())


"""Name rewriting"""

#curs.execute('UPDATE persons set name = "Michel" WHERE name = "Mike"')
#conn.commit()


"""Name delete"""

#curs.execute('DELETE FROM persons WHERE name = "Michel"')
#curs.execute('SELECT * FROM persons')
#print(curs.fetchall())
#conn.commit()


"""close"""

#curs.close()
#conn.close()



