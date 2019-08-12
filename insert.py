#!/usr/bin/env python3

# Script to insert all pictures from the camera db onto the projector db
# The actual pictures will need to be transferred over as well

import sqlite3

# Local
# DB_PROJECTOR = '/Users/Jordan/Developer/eds/capra-database/capra-projector.db'
# DB_CAMERA = '/Users/Jordan/Developer/eds/capra-database/capra-camera.db'

# External
DB_CAMERA = '/Volumes/capra-hd/capra_camera.db'
DB_PROJECTOR = '/Volumes/capra-hd/capra_projector.db'


def main():
    print('Starting the insert/transfer script')

    # Attach the camera to the projector database
    connection_projector = sqlite3.connect(DB_PROJECTOR)
    cursor_projector = connection_projector.cursor()
    attach_statement = "ATTACH '{db}' AS camera".format(db=DB_CAMERA)
    cursor_projector.execute(attach_statement)

    # Get number of pictures and hikes
    cursor_projector.execute("SELECT COUNT(*) FROM camera.pictures")
    all_rows = cursor_projector.fetchall()
    num_pics = all_rows[0][0]

    cursor_projector.execute("SELECT COUNT(*) FROM camera.hikes")
    all_rows = cursor_projector.fetchall()
    num_hikes = all_rows[0][0]

    # Insert Pictures
    cursor_projector.execute("SELECT * FROM camera.pictures")
    all_rows = cursor_projector.fetchall()
    picture_count = 0
    for row in all_rows:
        statement = "INSERT INTO pictures (time, altitude, color, hike, index_in_hike, camera1, camera2, camera3) VALUES ({t}, {a}, '{c}', {h}, {i}, '{c1}', '{c2}', '{c3}')".format(t=row[0], a=row[1], c=row[2], h=row[3], i=row[4], c1=row[5], c2=row[6], c3=row[7])
        cursor_projector.execute(statement)
        connection_projector.commit()
        picture_count = picture_count + 1
    print('Finished inserting {i} of {n} pictures from camera'.format(i=picture_count, n=num_pics))

    # Insert Hikes
    cursor_projector.execute("INSERT INTO hikes SELECT * FROM camera.hikes")
    connection_projector.commit()
    print('Finished inserting {n} hikes from camera'.format(n=num_hikes))


# def insert_pictures():
#     print('')

# def insert_hikes():
#     print('')

if __name__ == "__main__":
    main()
