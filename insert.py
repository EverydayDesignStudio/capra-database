#!/usr/bin/env python3

# Script to insert all pictures from the camera db onto the projector db
# The actual pictures will need to be transferred over as well

import sqlite3

DB_PROJECTOR = '/Users/Jordan/Developer/eds/capra-database/capra-projector.db'
DB_CAMERA = '/Users/Jordan/Developer/eds/capra-database/capra-camera.db'


def main():
    print('Starting the insert script')

    connection_projector = sqlite3.connect(DB_PROJECTOR)
    cursor_projector = connection_projector.cursor()
    attach_statment = "ATTACH '{db}' AS camera".format(db=DB_CAMERA)
    cursor_projector.execute(attach_statment)

    # Get number of pictures and hikes
    cursor_projector.execute("SELECT COUNT(*) FROM camera.pictures")
    all_rows = cursor_projector.fetchall()
    num_pics = all_rows[0][0]

    cursor_projector.execute("SELECT COUNT(*) FROM camera.hikes")
    all_rows = cursor_projector.fetchall()
    num_hikes = all_rows[0][0]

    # Execute statements
    cursor_projector.execute("INSERT INTO pictures SELECT * FROM camera.pictures")
    connection_projector.commit()
    print('Finished inserting {n} pictures from camera'.format(n=num_pics))

    cursor_projector.execute("INSERT INTO hikes SELECT * FROM camera.hikes")
    connection_projector.commit()
    print('Finished inserting {n} hikes from camera'.format(n=num_hikes))


if __name__ == "__main__":
    main()
