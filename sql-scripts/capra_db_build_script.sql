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
