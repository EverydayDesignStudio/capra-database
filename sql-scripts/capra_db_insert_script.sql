USE capra_db;

-- DELETE FROM hikes;

INSERT INTO hikes ("average_altitude", "average_color", "start_time", "end_time", "pictures", "created_date_time", "update_date_time") VALUES
	(90.82, '(161, 158, 129)', 1528704528, 1528705129, 240, datetime(), datetime()),
	(31.21, '(161, 158, 129)', 1528701481, 1528702079, 240, datetime(), datetime()),
	(1576.41, '(161, 158, 129)', 1530519742, 1530520343, 240, datetime(), datetime());

-- DELETE FROM pictures;

INSERT INTO pictures ("time", "altitude", "color", "hike", "index_in_hike", "camera1", "camera2", "camera3", "created_date_time", "update_date_time") VALUES
	(1528704528,90.82,'(135, 143, 138)',1,1,NULL,'/hike1/1.jpg',NULL,datetime(),datetime()),
	(1528704531,91.21,'(128, 128, 125)',1,2,NULL,'/hike1/2.jpg',NULL,datetime(),datetime()),
	(1528705126,46.79,'(64, 61, 56)',1,240,NULL,'/hike1/240.jpg',NULL,datetime(),datetime());