#!/usr/bin/env python3

import time
import sqlite3

DB_PROJECTOR = '/Users/Jordan/Developer/eds/capra-database/capra-projector.db'
DB_CAMERA = '/Users/Jordan/Developer/eds/capra-database/capra-camera.db'


def main():
    print('Starting the JOIN script')

    connection_projector = sqlite3.connect(DB_PROJECTOR)
    connection_camera = sqlite3.connect(DB_CAMERA)

    cursor_projector = connection_projector.cursor()
    cursor_projector.execute("ATTACH '/Users/Jordan/Developer/eds/capra-database/capra-projector.db' AS db1")
    cursor_projector.execute("ATTACH '/Users/Jordan/Developer/eds/capra-database/capra-camera.db' AS db2")

    # cursor_projector.execute("SELECT * FROM db1.pictures")
    cursor_projector.execute("INSERT INTO pictures SELECT * FROM db2.pictures")
    connection_projector.commit()

    # all_rows = cursor_projector.fetchall()
    # for row in all_rows:
    #     print(row)

    # all_rows = cursor.fetchall()
    # picture = self._build_picture_from_row(all_rows[0])
    # return picture

    print('Finished the command(s)')

if __name__ == "__main__":
    main()
