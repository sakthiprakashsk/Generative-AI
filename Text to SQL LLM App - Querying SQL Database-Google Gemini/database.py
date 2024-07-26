import sqlite3


connection = sqlite3.connect("student.db")

cursor= connection.cursor()

table_info = """
Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25), MARKS INT)
"""

cursor.execute(table_info)

cursor.execute('''Insert Into STUDENT values('Krish', 'Data Sience', 'A', '90')''')
cursor.execute('''Insert Into STUDENT values('Naik', 'Data Sience', 'B', '100')''')
cursor.execute('''Insert Into STUDENT values('Darius', 'Data Sience', 'A', '80')''')
cursor.execute('''Insert Into STUDENT values('Vikas', 'DEVOPS', 'A', '50')''')
cursor.execute('''Insert Into STUDENT values('Dipesh', 'DEVOPS', 'A', '40')''')

print("Records are...")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)
    

connection.commit()
connection.close()