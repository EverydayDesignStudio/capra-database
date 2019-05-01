#!/usr/bin/env python3

import time
import sqlite3
from sql_parser import SQLParser
from sql_statements import SQLStatements

SQLITE_DB = 'capra.db'
statements = SQLStatements()


def main():
    print('Starting SQLite3 program')

    connection = sqlite3.connect(SQLITE_DB)
    # get_picture(connection, 1, 54)
    time_for_full_hike(connection)


def time_for_full_hike(connection):
    start_time = time.time()
    cursor = connection.cursor()
    index = 1
    while index <= 240:
        cursor.execute(statements.select_photo(1, index))
        index += 1
        all_rows = cursor.fetchall()
        print(all_rows[0])

    end_time = time.time()
    print('start: ' + str(start_time))
    print('end: ' + str(end_time))
    print(end_time - start_time)


def get_picture(connection, hike_id, index_in_hike) -> None:
    cursor = connection.cursor()
    cursor.execute(statements.select_photo(hike_id, index_in_hike))
    all_rows = cursor.fetchall()
    print(all_rows[0][1])
    # for row in all_rows:
    #     print(row[0])


# def create_db(c):
#     # Create a new SQLite table with 1 column
#     c.execute('CREATE TABLE {tn} ({nf} {ft})\
#         '.format(tn=TABLE_NAME_1, nf=COLUMN_1, ft=FIELD_TYPE))

#     # Create 2nd table with 1 column and set it as PRIMARY KEY
#     c.execute('CREATE TABLE {tn} ({nf} {ft} PRIMARY KEY)\
#         '.format(tn=TABLE_NAME_2, nf=COLUMN_1, ft=FIELD_TYPE))

#     # Commit changes and close connection
#     connection.commit()
#     connection.close()


# def query_db_id(c, id):
#     c.execute('SELECT * FROM {tn} WHERE {idf}={my_id}\
#         '.format(tn=TABLE_NAME_2, cn=COLUMN_2, idf=COLUMN_1, my_id=id))
#     id_exists = c.fetchone()
#     if id_exists:
#         print('5): {}'.format(id_exists))
#     else:
#         print('5): {} does not exist'.format(id))


# def query_db_allrows(c, keyword):
#     # Contents of all columns for row that match certain value in column1
#     c.execute('SELECT * FROM {tn} WHERE {cn}="{kw}"\
#         '.format(tn=TABLE_NAME_1, cn=COLUMN_1, kw=keyword))
#     all_rows = c.fetchall()
#     print(all_rows)

if __name__ == "__main__":
    main()
