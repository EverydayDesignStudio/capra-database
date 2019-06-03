CREATE DATABASE capra_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE capra_db;

DROP TABLE IF EXISTS "hikes";

CREATE TABLE "hikes" (
	"hike_id"	INTEGER UNIQUE,
	"average_altitude"	REAL,
	"average_color"	TEXT,
	"start_time"	REAL UNIQUE,
	"end_time"	REAL UNIQUE,
	"pictures"	INTEGER,
	"created_date_time" REAL DEFAULT CURRENT_TIMESTAMP,
	"updated_date_time" REAL DEFAULT CURRENT_TIMESTAMP
);

DROP TABLE IF EXISTS "pictures";

CREATE TABLE "pictures" (
	"picture_id"	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
	"time"	REAL,
	"altitude"	REAL,
	"color"	TEXT,
	"hike"	INTEGER,
	"index_in_hike"	INTEGER,
	"camera1"	TEXT,
	"camera2"	TEXT,
	"camera3"	TEXT,
	"created_date_time" REAL DEFAULT CURRENT_TIMESTAMP,
	"updated_date_time" REAL DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY("hike") REFERENCES "hikes"("hike_id")
);



/* Average Altitude */
SELECT AVG(altitude) FROM pictures WHERE hike=8;

/* First Time */
SELECT time FROM pictures WHERE hike=8 ORDER BY time ASC LIMIT 1;

/* Last Time */
SELECT time FROM pictures WHERE hike=8 ORDER BY time DESC LIMIT 1;

/* Count of hike pictures */
SELECT count(*) FROM pictures WHERE hike=8;





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
