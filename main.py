#!/usr/bin/env python3

import sqlite3

SQLITE_FILE = 'my_first_db.sqlite'
TABLE_NAME_1 = 'my_table_1'
TABLE_NAME_2 = 'my_table_2'
COLUMN_1 = 'my_1st_column'
COLUMN_2 = 'my_2nd_column'
COLUMN_3 = 'my_3rd_column'
FIELD_TYPE = 'INTEGER'

connection = sqlite3.connect(SQLITE_FILE)
cursor = connection.cursor()

def main():
    print('Starting SQLite3 program')
    
    # create_db(cursor)
    # query_db_allrows(cursor, 'HEY WORLD')
    query_db_id(cursor, 10)

def create_db(c):
    # Create a new SQLite table with 1 column
    c.execute('CREATE TABLE {tn} ({nf} {ft})'.format(tn=TABLE_NAME_1, nf=COLUMN_1, ft=FIELD_TYPE))

    # Create 2nd table with 1 column and set it as PRIMARY KEY
    c.execute('CREATE TABLE {tn} ({nf} {ft} PRIMARY KEY)'.format(tn=TABLE_NAME_2, nf=COLUMN_1, ft=FIELD_TYPE))

    # Commit changes and close connection
    connection.commit()
    connection.close()

def query_db_id(c, id):
    c.execute('SELECT * FROM {tn} WHERE {idf}={my_id}'.\
        format(tn=TABLE_NAME_2, cn=COLUMN_2, idf=COLUMN_1, my_id=id))
    id_exists = c.fetchone()
    if id_exists:
        print('5): {}'.format(id_exists))
    else:
        print('5): {} does not exist'.format(id))

def query_db_allrows(c, keyword):
    # Contents of all columns for row that match certain value in column1
    c.execute('SELECT * FROM {tn} WHERE {cn}="{kw}"'.format(tn=TABLE_NAME_1, cn=COLUMN_1, kw=keyword))
    all_rows = c.fetchall()
    print(all_rows)

if __name__ == "__main__": main()
