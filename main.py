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
except mysql.connector.Error as err:
    print('Unable to connect: {}'.format(err))
cursor = connection.cursor()

autocorrect_query = cursor.execute("SELECT Expression FROM Dictionary")
autocorrect_list = cursor.fetchall()
autocorrect = []
for entry in autocorrect_list:
    autocorrect.append(entry[0])
autocorrect = list(dict.fromkeys(autocorrect))

word = ' '
while word != '0':
    query_var = None
    word = input('Enter word: ')
    if word == '0':
        output = 'Goodbye'
        pass
    elif word in autocorrect:
        query_var = word
    elif word not in autocorrect:
        suggestion = close_matches(word, autocorrect, 5, 0.7)
        if suggestion:
            for option in suggestion:
                corrected_word = input(f'Did you mean "{option}"? (y/n): ')
                if corrected_word == 'y':
                    query_var = option
                    break
            if corrected_word != 'y':
                output = ['Word not found.', 'Try again']
        else:
            output = ['Word not found.', 'Try again']
    if query_var is not None:
        # add a try statement here
        cursor.execute(f"Select * FROM Dictionary WHERE Expression = '{query_var}'")
        row = cursor.fetchone()
        for row in cursor:
            print(row[1])
    else:
        print(output)
