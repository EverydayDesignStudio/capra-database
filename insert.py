#!/usr/bin/env python3

# Script to insert all pictures from the camera db onto the projector db
# The actual pictures will need to be transferred over as well

import sqlite3

# Local
# DB_PROJECTOR = '/Users/Jordan/Developer/eds/capra-database/capra-projector.db'
# DB_CAMERA = '/Users/Jordan/Developer/eds/capra-database/capra-camera.db'

# External (Mac)
DB_CAMERA = '/Volumes/capra-hd/capra_camera.db'
# DB_CAMERA = '/Volumes/capra-hd/capra-projector-jordan-hike.db'
DB_PROJECTOR = '/Volumes/capra-hd/capra_projector.db'

# External (Raspberry Pi)
# DB_CAMERA = '/media/pi/capra-hd/capra_camera.db'
# DB_PROJECTOR = '/media/pi/capra-hd/capra_projector.db'


def main():
    print('Starting the insert/transfer script')

    # Attach the camera to the projector database
    connection_projector = sqlite3.connect(DB_PROJECTOR)
    cursor_projector = connection_projector.cursor()
    attach_statement = "ATTACH '{db}' AS camera".format(db=DB_CAMERA)
    cursor_projector.execute(attach_statement)

    # Insert Pictures
    insert_pictures(connection_projector, cursor_projector)

    # Insert Hikes
    insert_hikes(connection_projector, cursor_projector)

    # TODO test this functionality first
    # Delete the pictures and hikes on the camera database
    # delete_pictures_hikes(connection_projector, cursor_projector)


def insert_pictures(connection: sqlite3.Connection, cursor: sqlite3.Connection.cursor):
    # Get number of pictures
    cursor.execute("SELECT COUNT(*) FROM camera.pictures")
    all_rows = cursor.fetchall()
    num_pics = all_rows[0][0]

    # Insert all pictures
    cursor.execute("SELECT * FROM camera.pictures")
    all_rows = cursor.fetchall()
    picture_count = 0
    for row in all_rows:
        print(row)
        # statement_jordan = "INSERT INTO pictures (time, altitude, hike, index_in_hike, camera1, camera2, camera3) VALUES ({t}, {a}, {h}, {i}, '{c1}', '{c2}', '{c3}')".format(t=row[1], a=row[2], h=row[4], i=row[5], c1=row[6], c2=row[7], c3=row[8])

        statement = "INSERT INTO pictures (time, altitude, hike, index_in_hike, camera1, camera2, camera3) VALUES ({t}, {a}, {h}, {i}, '{c1}', '{c2}', '{c3}')".format(t=row[0], a=row[1], h=row[3], i=row[4], c1=row[5], c2=row[6], c3=row[7])
        cursor.execute(statement)
        connection.commit()
        picture_count += 1
    print('Finished inserting {i} of {n} pictures from camera'.format(i=picture_count, n=num_pics))


def insert_hikes(connection: sqlite3.Connection, cursor: sqlite3.Connection.cursor):
    # Get number of hikes
    cursor.execute("SELECT COUNT(*) FROM camera.hikes")
    all_rows = cursor.fetchall()
    num_hikes = all_rows[0][0]

    # Insert all hikes
    cursor.execute("SELECT * FROM camera.hikes")
    all_rows = cursor.fetchall()
    hike_count = 0
    for row in all_rows:
        print(row)
        # statement_jordan = "INSERT INTO hikes (hike_id, avg_altitude, start_time, end_time, pictures) VALUES ({id}, {aa}, {st}, {et}, {p})".format(id=row[0], aa=row[1], st=row[3], et=row[4], p=row[5])

        statement = "INSERT INTO hikes (hike_id, start_time, end_time, pictures, path) VALUES ({id}, {st}, {et}, {p}, '{pth}')".format(id=row[0], st=row[3], et=row[4], p=row[5], pth=row[6])
        cursor.execute(statement)
        connection.commit()
        hike_count += 1
    print('Finished inserting {i} of {n} hikes from camera'.format(i=hike_count, n=num_hikes))

    # Old Insert Hikes
    # cursor_projector.execute("INSERT INTO hikes SELECT * FROM camera.hikes")
    # connection_projector.commit()
    # print('Finished inserting {n} hikes from camera'.format(n=num_hikes))


def delete_pictures_hikes(connection: sqlite3.Connection, cursor: sqlite3.Connection.cursor):
    cursor.execute("DELETE FROM camera.pictures")
    connection.commit()
    cursor.execute("DELETE FROM camera.hikes")
    connection.commit()


if __name__ == "__main__":
    main()
