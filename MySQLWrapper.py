# -*- coding: UTF-8 -*-

import mysql.connector

class MySQLWrapper:

    def __init__(self):
        self.cnx    = mysql.connector.connect(user='root', database='test_db')
        self.cursor = self.cnx.cursor()


    def insert(self, key, val):
        query = ("""INSERT INTO  `test_table` (  `keys` ,  `data` ) VALUES (%s,%s)""")
        self.cursor.execute(query, (key,val))
        self.cnx.commit()

        return self.cursor.rowcount


    def select(self, key):
        query = ("SELECT * FROM test_table WHERE test_table.keys=%s")
        self.cursor.execute(query, (key,))

        return self.cursor.fetchall()


    def update(self, key, val):
        query = ("""UPDATE test_table SET `data`=%s WHERE `keys`=%s""")
        self.cursor.execute(query, (val,key))
        self.cnx.commit()

        return self.cursor.rowcount


    def __del__(self):
        self.cursor.close()
        self.cnx.close()


if __name__ == '__main__':
    pass
