----------------------------------------------------------------
-- CAMERA BUILD
CREATE DATABASE capra_camera CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE capra_camera;

DROP TABLE IF EXISTS "hikes";

CREATE TABLE "hikes" (
	"hike_id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"average_altitude"	REAL,
	"average_color"	TEXT,
	"start_time"	REAL UNIQUE,
	"end_time"	REAL UNIQUE,
	"pictures"	INTEGER,
	"created_date_time" TEXT DEFAULT CURRENT_TIMESTAMP,
	"updated_date_time" TEXT DEFAULT CURRENT_TIMESTAMP
);

DROP TABLE IF EXISTS "pictures";

-- no picture_id, this is added upon transfer back to projector
CREATE TABLE "pictures" (
	"time"	REAL UNIQUE,
	"altitude"	REAL,
	"color"	TEXT,
	"hike"	INTEGER,
	"index_in_hike"	INTEGER,
	"camera1"	TEXT,
	"camera2"	TEXT,
	"camera3"	TEXT,
	"created_date_time" TEXT DEFAULT CURRENT_TIMESTAMP,
	"updated_date_time" TEXT DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY("hike") REFERENCES "hikes"("hike_id")
);


----------------------------------------------------------------
-- PROJECTOR BUILD
CREATE DATABASE capra_projector CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE capra_projector;

DROP TABLE IF EXISTS "hikes";

-- hike_id is not PRIMARY KEY AUTOINCREMENT since it will never be incremented on the projector
-- and on off case it is, it could get out of sync with camera
CREATE TABLE "hikes" (
	"hike_id"	INTEGER UNIQUE,
	"average_altitude"	REAL,
	"average_color"	TEXT,
	"start_time"	REAL UNIQUE,
	"end_time"	REAL UNIQUE,
	"pictures"	INTEGER,
	"created_date_time" TEXT DEFAULT CURRENT_TIMESTAMP,
	"updated_date_time" TEXT DEFAULT CURRENT_TIMESTAMP
);

DROP TABLE IF EXISTS "pictures";

-- picture_id is here, but not in CAMERA db
CREATE TABLE "pictures" (
	"picture_id"	INTEGER PRIMARY KEY UNIQUE,
	"time"	REAL UNIQUE,
	"altitude"	REAL,
	"color"	TEXT,
	"hike"	INTEGER,
	"index_in_hike"	INTEGER,
	"camera1"	TEXT,
	"camera2"	TEXT,
	"camera3"	TEXT,
	"created_date_time" TEXT DEFAULT CURRENT_TIMESTAMP,
	"updated_date_time" TEXT DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY("hike") REFERENCES "hikes"("hike_id")
);


----------------------------------------------------------------
-- Inserts into hikes and pictures on PROJECTOR DB
INSERT INTO hikes (hike_id, average_altitude, average_color, start_time, end_time, pictures, created_date_time, updated_date_time) VALUES ({h}, {a}, '{c}', {st}, {et}, {p}, {cd}, {ud})

INSERT INTO pictures (time, altitude, color, hike, index_in_hike, camera1, camera2, camera3, created_date_time, updated_date_time) VALUES ({t}, {a}, '{c}', {h}, {i}, '{c1}', '{c2}', '{c3}', {cd}, {ud})


----------------------------------------------------------------
-- Delete all items from a table
DELETE FROM hikes;
DELETE FROM pictures;


----------------------------------------------------------------
-- Calculate Values where hike=4

-- Average Altitude
SELECT AVG(altitude) FROM pictures WHERE hike=4;

-- Calculate Average Color
-- python.script()

-- First Time
SELECT time FROM pictures WHERE hike=4 ORDER BY time ASC LIMIT 1;

-- Last Time
SELECT time FROM pictures WHERE hike=4 ORDER BY time DESC LIMIT 1;

-- Count of hike pictures
SELECT count(*) FROM pictures WHERE hike=4;


/* 
def create_db(c):
	# Create a new SQLite table with 1 column
	c.execute('CREATE TABLE {tn} ({nf} {ft})\
		'.format(tn=TABLE_NAME_1, nf=COLUMN_1, ft=FIELD_TYPE))

 	# Create 2nd table with 1 column and set it as PRIMARY KEY
	c.execute('CREATE TABLE {tn} ({nf} {ft} PRIMARY KEY)\
		'.format(tn=TABLE_NAME_2, nf=COLUMN_1, ft=FIELD_TYPE))

	# Commit changes and close connection
	connection.commit()
	connection.close()
*/

/*
def query_db_id(c, id):
    c.execute('SELECT * FROM {tn} WHERE {idf}={my_id}\
        '.format(tn=TABLE_NAME_2, cn=COLUMN_2, idf=COLUMN_1, my_id=id))
    id_exists = c.fetchone()
    if id_exists:
        print('5): {}'.format(id_exists))
    else:
        print('5): {} does not exist'.format(id))
*/

/*
def query_db_allrows(c, keyword):
    # Contents of all columns for row that match certain value in column1
    c.execute('SELECT * FROM {tn} WHERE {cn}="{kw}"\
        '.format(tn=TABLE_NAME_1, cn=COLUMN_1, kw=keyword))
    all_rows = c.fetchall()
    print(all_rows)
*/
