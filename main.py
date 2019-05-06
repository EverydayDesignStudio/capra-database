#!/usr/bin/env python3

import getch
import time
import sqlite3
from capra_data_types import Picture, Hike
from sql_controller import SQLController


def main():
    while True:
        # char = getch.getch()
        # if char == '-':
        #     print('NEXT')
        # elif char == '-':
        #     print('PREVIOUS')

        keycode = ord(getch.getch())

        if keycode == 67:
            print('NEXT')
        elif keycode == 68:
            print('PREVIOUS')
        elif keycode == 109:
            print('CHANGE MODE')
        


    # print('Starting SQLite3 program')

    # current_picture = Picture()
    # current_hike = Hike()

    # sql_controller = SQLController()
    # current_picture = sql_controller.get_first_time_picture()
    # print(current_picture.altitude)

    # count = 1
    # while count < 100:
    #     current_picture = sql_controller.next_altitude_picture(current_picture)
    #     print('altitude: ' + str(current_picture.altitude) + '  |  time: ' + str(current_picture.time))
    #     count += 1

    # sql_controller.next_altitude_picture(current_picture)

    # get_picture(connection, 1, 54)
    # get_picture(connection, 1, 94)
    # time_for_full_hike(connection)


# def time_for_full_hike(connection):
#     start_time = time.time()
#     cursor = connection.cursor()
#     index = 1
#     while index <= 240:
#         cursor.execute(statements.select_picture(1, index))
#         index += 1
#         all_rows = cursor.fetchall()
#         print(all_rows[0])

#     end_time = time.time()
#     print('start: ' + str(start_time))
#     print('end: ' + str(end_time))
#     print(end_time - start_time)


# def get_picture(connection, hike_id, index_in_hike) -> None:
#     cursor = connection.cursor()
#     cursor.execute(statements.select_picture(hike_id, index_in_hike))
#     all_rows = cursor.fetchall()
#     print(all_rows[0])

#     # for row in all_rows:
#     #     print(row[0])

#     connection.commit()
#     # connection.close()


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
