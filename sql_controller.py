# Controller to handle UI talking with the SQLite database

import sqlite3
from capra_data_types import Picture, Hike
from sql_statements import SQLStatements

SQLITE_DB = 'capra.db'


class SQLController:
    def __init__(self):
        self.connection = sqlite3.connect(SQLITE_DB)
        self.statements = SQLStatements()

    # Helper methods
    def build_picture_from_row(self, row: list) -> Picture:
        picture = Picture(picture_id=row[0], time=row[1], altitude=row[2],
                          color=row[3], hike_id=row[4], index_in_hike=row[5],
                          camera1=row[6], camera2=row[7], camera3=row[8])
        return picture

    # Time
    def get_first_time_picture(self) -> Picture:
        cursor = self.connection.cursor()
        cursor.execute(self.statements.selct_by_time_first_picture())
        all_rows = cursor.fetchall()
        picture = self.build_picture_from_row(all_rows[0])
        return picture

    def get_last_time_picture(self) -> Picture:
        cursor = self.connection.cursor()
        cursor.execute(self.statements.selct_by_time_last_picture())
        all_rows = cursor.fetchall()
        picture = self.build_picture_from_row(all_rows[0])
        return picture

    # Altitude
    def next_altitude_picture(self, current_picture: Picture) -> Picture:
        cursor = self.connection.cursor()
        t = current_picture.time
        alt = current_picture.altitude

        cursor.execute(self.statements.find_size_by_altitude(altitude=alt, time=t))
        all_rows = cursor.fetchall()
        count = all_rows[0][0]
        print(count)

        if count == 0:
            cursor.execute(self.statements.select_by_greater_altitude_next_picture(altitude=alt))
        elif count > 0:
            print('here')
            cursor.execute(self.statements.select_by_equal_altitude_next_picture(altitude=alt, time=t))

        all_rows = cursor.fetchall()
        print(all_rows[0])
        picture = self.build_picture_from_row(all_rows[0])
        return picture
