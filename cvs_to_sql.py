# Controller to handle UI talking with the SQLite database

import csv
import sqlite3
from capra_data_types import Picture, Hike
from sql_statements import SQLStatements

# SQLITE_DB = 'capra.db'
SQLITE_DB = '/Volumes/Capra/capra-projector.db'


class CSVtoSQL:
    def __init__(self):
        self.connection = sqlite3.connect(SQLITE_DB)
        self.statements = SQLStatements()

    def add(self):
        for i in range(8, 16):
            self.add_hike_from_csv(i)

            path = f'/Volumes/Capra/jordan-hike{i}/meta.csv'
            folder = f'/jordan-hike{i}'
            self.add_pictures_from_csv(path, i, folder)

    def add_hike_from_csv(self, hike: float):
        cursor = self.connection.cursor()

        average_statement = 'SELECT AVG(altitude) FROM pictures WHERE hike={h}'.format(h=hike)
        cursor.execute(average_statement)
        result = cursor.fetchall()
        alt = round(result[0][0], 2)

        start_statement = 'SELECT time FROM pictures WHERE hike={h} ORDER BY time ASC LIMIT 1'.format(h=hike)
        cursor.execute(start_statement)
        result = cursor.fetchall()
        start = round(result[0][0], 0)

        start_statement = 'SELECT time FROM pictures WHERE hike={h} ORDER BY time DESC LIMIT 1'.format(h=hike)
        cursor.execute(start_statement)
        result = cursor.fetchall()
        end = round(result[0][0], 0)

        pics_statement = 'SELECT count(*) FROM pictures WHERE hike={h}'.format(h=hike)
        cursor.execute(pics_statement)
        result = cursor.fetchall()
        pics = result[0][0]

        color = 'rgb'

        insert_statement = f'INSERT INTO hikes \
                      (hike_id, average_altitude, average_color, start_time, end_time, pictures) VALUES \
                      ({hike}, {alt}, "{color}", {start}, {end}, {pics})'
        print(insert_statement)
        cursor.execute(insert_statement)
        self.connection.commit()

        print(f'Added information from hike {hike}')

    def add_pictures_from_csv(self, file: str, hike: float, prefix: str):
        cursor = self.connection.cursor()

        with open(file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            csv_file.readline()
            for row in csv_reader:
                index = row[0]
                time = round(float(row[1]), 0)
                altitude = round(float(row[2]), 2)
                color = 'rgb'
                c1 = f'{prefix}{index}_cam1.jpg'
                c2 = f'{prefix}{index}_cam2.jpg'
                c3 = f'{prefix}{index}_cam3.jpg'
                statement = f'INSERT INTO pictures \
                            (time, altitude, color, hike, index_in_hike, camera1, camera2, camera3) VALUES \
                            ({time}, {altitude}, "{color}", {hike}, {index}, "{c1}", "{c2}", "{c3}")'
                cursor.execute(statement)
                self.connection.commit()

        # self.connection.close()
        print(f'Imported all pictures from hike {hike}')
