USE capra_camera;

-- Create a new hike
INSERT INTO hikes (average_altitude, average_color, start_time, end_time, pictures, created_date_time, updated_date_time) VALUES
	(0.0, 'rgb', {st}, NULL, 0, datetime(), datetime())

-- Grab the last hike_id
SELECT hike_id FROM hikes ORDER BY hike_id DESC LIMIT 1;

-- Create a new picture
INSERT INTO pictures (time, altitude, color, hike, index_in_hike, camera1, camera2, camera3, created_date_time, updated_date_time) VALUES 
	({t}, {a}, '{c}', {h}, {i}, '{c1}', '{c2}', '{c3}', datetime(), datetime())


-- Scripts that might help
UPDATE pictures SET hike = 8 WHERE hike = 15;

SELECT *  FROM hikes WHERE path LIKE '/home/pi/%'

SELECT replace(path, '/home/pi/capra-storage/', '/media/pi/capra-hd/') FROM hikes;
UPDATE hikes SET path = replace(path, '/home/pi/capra-storage/', '/media/pi/capra-hd/');

-- jordan-hikes
UPDATE pictures SET camera1 = replace(camera1, '/jordan-hike15/', '/media/pi/capra-hd/hike8/');
UPDATE pictures SET camera2 = replace(camera2, '/jordan-hike15/', '/media/pi/capra-hd/hike8/');
UPDATE pictures SET camera3 = replace(camera3, '/jordan-hike15/', '/media/pi/capra-hd/hike8/');

SELECT count(DISTINCT time) FROM pictures;

SELECT * FROM pictures WHERE altitude IS NULL;