import sqlite3, csv

connection = sqlite3.connect("deliveries.db")
connection1 = sqlite3.connect("matches.db")
cursor = connection.cursor()

with open('x_matches.csv', 'r') as file:
    no_records = 0
    for row in file:
        if no_records == 0:
            no_records +=1
            continue
        print(row)
        connection1.execute("INSERT INTO Matches VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", row.split(","))
        connection1.commit()
        no_records += 1
        print(no_records)
connection1.close()

print('\n{} Records Transferred'.format(no_records))

