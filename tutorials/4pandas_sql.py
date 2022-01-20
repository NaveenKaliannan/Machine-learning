
import numpy as np
import pandas as pd
import sqlite3


create_table= """
CREATE TABLE studentscore
(id INTEGER, Name VARAD(20), Math REAL,
Science REAL
);"""

executeSQL=sqlite3.connect(':memory:')
executeSQL.execute(create_table)
executeSQL.commit()

SQL_query=executeSQL.execute('select * from studentscore')
resulset = SQL_query.fetchall()
print(resulset)

insertSQL = [(10,'Jack',85,92), (29,'Tom',73,89)]
insert_statement="Insert into studentscore values (?,?,?,?)"
executeSQL.executemany(insert_statement,insertSQL)
executeSQL.commit()

SQL_query = executeSQL.execute("select * from studentscore")
resulset = SQL_query.fetchall()
print(resulset)

df_student = pd.DataFrame(resulset, columns=zip(*SQL_query.description)[0])
print(df_student)
