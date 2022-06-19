    """This module is used to look at the data that was imported from
    the complaints data online
    """

import sqlite3

conn = sqlite3.connect("E:\Projects\GRYPAR\webagent\db.sqlite3")

cursor = conn.cursor()
#set the limite to 10 for testing and viewing data
cursor.execute("SELECT * FROM  'consumer-complaints-QueryResult' limit 100 ")
rows = cursor.fetchall()
type(rows)