# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 11:22:23 2022

@author: sudhakar.sinha
"""

import pyodbc 

conn = pyodbc.connect('''DRIVER={ODBC Driver 17 for SQL Server};
                  SERVER=(localdb)\MSSQLLocalDB;
                  PORT=1433;
                  DATABASE=quantifypalnetwork;
                  Trusted_Connection=yes;''')

cursor = conn.cursor()
cursor.execute('SELECT * FROM project')

for i in cursor:
    print(i)