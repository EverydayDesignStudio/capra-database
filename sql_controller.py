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
    def _build_picture_from_row(self, row: list) -> Picture:
        picture = Picture(picture_id=row[0], time=row[1], altitude=row[2],
                          color=row[3], hike_id=row[4], index_in_hike=row[5],
                          camera1=row[6], camera2=row[7], camera3=row[8])
        return picture

    def _get_picture_from_sql_statement(self, statement: str) -> Picture:
        cursor = self.connection.cursor()
        cursor.execute(statement)
        all_rows = cursor.fetchall()
        picture = self._build_picture_from_row(all_rows[0])
        return picture

    # Time
    def get_first_time_picture(self) -> Picture:
        sql = self.statements.select_by_time_first_picture()
        return self._get_picture_from_sql_statement(sql)

    def get_last_time_picture(self) -> Picture:
        sql = self.statements.select_by_time_last_picture()
        return self._get_picture_from_sql_statement(sql)

    # Altitude - get starting picture
    def get_greatest_altitude_picture(self) -> Picture:
        sql = self.statements.select_by_altitude_greatest_picture()
        return self._get_picture_from_sql_statement(sql)

    def get_least_altitude_picture(self) -> Picture:
        sql = self.statements.select_by_altitude_least_picture()
        return self._get_picture_from_sql_statement(sql)

    # Altitude - next & previous across hikes
    def next_altitude_picture_across_hikes(self, current_picture: Picture) -> Picture:
        cursor = self.connection.cursor()
        t = current_picture.time
        alt = current_picture.altitude

        cursor.execute(self.statements.find_size_by_altitude_greater_time(altitude=alt, time=t))
        all_rows = cursor.fetchall()
        count = all_rows[0][0]
        print(count)

        if count == 0:
            cursor.execute(self.statements.select_by_greater_altitude_next_picture(altitude=alt))
        elif count > 0:
            cursor.execute(
                self.statements.select_by_equal_altitude_next_picture(altitude=alt, time=t))
        all_rows = cursor.fetchall()

        # end of the list of altitudes, loop back around to least altitude
        if not all_rows:
            return self.get_least_altitude_picture()
        else:  # there is a next picture
            return self._build_picture_from_row(all_rows[0])

    def previous_altitude_picture_across_hikes(self, current_picture: Picture) -> Picture:
        cursor = self.connection.cursor()
        t = current_picture.time
        alt = current_picture.altitude

        cursor.execute(self.statements.find_size_by_altitude_less_time(altitude=alt, time=t))
        all_rows = cursor.fetchall()
        count = all_rows[0][0]

        if count == 0:
            cursor.execute(self.statements.select_by_less_altitude_previous_picture(altitude=alt))
        elif count > 0:
            cursor.execute(
                self.statements.select_by_equal_altitude_previous_picture(altitude=alt, time=t))
        all_rows = cursor.fetchall()

        # end of the list of altitudes, loop back around to greatest altitude
        if not all_rows:
            return self.get_greatest_altitude_picture()
        else:  # there is a previous picture
            return self._build_picture_from_row(all_rows[0])

    # Altitude - next & previous in one hike
