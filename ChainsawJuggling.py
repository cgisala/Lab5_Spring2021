#This program stores the information of chairsaw juggling record holder as of July 2018

import sqlite3
import traceback

db = 'sqldatabase.db'

def main():

    banner()
    while True:
        try:
            menu() # prints menu
            option = input('What is your choice? ') 
            menu_option(option, db)
            
            choice = input('\nDo you wish to continue? y or n: ').lower() # prompts the user to continue or not
            if choice == 'n':
                break
            else:
                conn = sqlite3.connect('sqldatabase.db') 
                cur = conn.execute('select * from record_holders_2018')

                banner()
                # Print all the data in the table
                for row in cur:
                    print(row)

                conn.close() # Close connection
        except Exception:
            traceback.print_exc()

def banner():
    print("\n************************************************")
    print("Chainsaw Juggling Record Holders as of July 2018")
    print("************************************************")

def menu():
    print('\nMENU: \n'
        '1: Add a new record\n'
        '2: Update a record\n'
        '3: Delete a record\n'
        '4: Search a database\n')

def menu_option(option, db):
    if option == '1':
        add_new_row(db)
    elif option == '2':
        update_catches(db)
    elif option == '3':
        delete_record(db)
    elif option == '4':
        search_record_holder(db)
    else:
        print('\nYour choice is not in the menu. Try again.')

def add_new_row(db):
    #Creates or opens connection to the db file
    conn = sqlite3.connect(db)

    #Ask the user for information about the juggler
    print('\nEnter the Juggler info:')
    name = input('Name: ').title()
    country = input('Country: ').title()
    catches = input('Number of catches: ').title()

    #Inserts the name, country, and catches in the database
    conn.execute('insert into record_holders_2018 values (?,?,?)', (name, country, catches))
    conn.commit()  # Saves changes to database
    conn.close()  # Close connection

def update_catches(db):
    print('\nTo update a record enter the following:')
    name = input('Name: ').title()
    catches = int(input('Number of catches: '))

    conn = sqlite3.connect(db) # createsor opens connection to db file

    # Update the number of catches of the juggler record
    conn.execute('Update record_holders_2018 SET number_of_catches = ? WHERE name = ?', (catches, name))
    conn.commit() # save changes to database
    conn.close() # clsoe connection

def delete_record(db):
    print('\nTo delete a record enter the following:')
    name = input('Name: ').title()

    conn = sqlite3.connect(db) # create or opens connection to db file
    curs = conn.cursor()
    curs.execute("DELETE FROM record_holders_2018 WHERE name = (?)", (name,))
    conn.commit() # save changes to database
    conn.close() # close connection

def search_record_holder(db):
    print('\nTo search the database enter the following:')
    name = input('Name: ').title()

    # Get the record from the database by name
    record = 'SELECT name, * FROM record_holders_2018 WHERE name = ?'
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row # row_factory allows access to data by row name
    rows = conn.execute(record, (name,) )
    juggler_record = rows.fetchone() # Get first result

    print('\nJugger Record:')

    print(juggler_record['name'], juggler_record['country'], juggler_record['number_of_catches']) # Print juggler info
    conn.close()

if __name__=='__main__':
    main()