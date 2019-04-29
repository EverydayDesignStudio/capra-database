CREATE DATABASE capra_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE capra_db;

DROP TABLE IF EXISTS "hikes";

CREATE TABLE "hikes" (
	"hike_id"	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
	"average_altitude"	REAL,
	"average_color"	TEXT,
	"start_time"	REAL UNIQUE,
	"end_time"	REAL UNIQUE,
	"pictures"	INTEGER,
	"created_date_time" REAL DEFAULT CURRENT_TIMESTAMP,
	"update_date_time" REAL DEFAULT CURRENT_TIMESTAMP
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
	"update_date_time" REAL DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY("hike") REFERENCES "hikes"("hike_id")
);
