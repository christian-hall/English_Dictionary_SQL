import mysql.connector
from difflib import get_close_matches as close_matches

print('Welcome to the English Dictionary - SQL Edition')
print('Enter "0" at any time to quit the program')
try:
    connection = mysql.connector.connect(
        user='ardit700_student',
        password='ardit700_student',
        host='108.167.140.122',  # this is the ip address of this particular database
        database='ardit700_pm1database'
    )
    cursor = connection.cursor()
except mysql.connector.Error as err:
    print('Unable to connect: {}'.format(err))

entry = input('Enter a word : ')

query = cursor.execute(f"SELECT * FROM Dictionary WHERE Expression = '{entry}'")
results = cursor.fetchall()

if results:
    for result in results:
        print(result[1])

else:
    print('No word found')
