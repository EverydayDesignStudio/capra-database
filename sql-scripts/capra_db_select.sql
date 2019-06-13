USE capra_db;

--------------------------------------------------------------------------
-- Working
SELECT * FROM pictures 
WHERE altitude>=101.71 
ORDER BY altitude ASC, time ASC;

SELECT * FROM pictures WHERE altitude>= 90
ORDER BY
(CASE
	WHEN  altitude > 101 THEN "hello world"
	ELSE time
END) ASC;

SELECT *, count(1)
FROM pictures WHERE altitude >= 101.71
GROUP BY altitude
HAVING count(1) > 1
ORDER BY picture_id;


--------------------------------------------------------------------------
-- Current Picture:
-- altitude = 101.71
-- time = 1528704661.0
SELECT count(*) FROM pictures WHERE altitude=101.71;

-- If count > 1
SELECT * FROM pictures WHERE altitude=101.71 AND time>1528704661.0
ORDER BY time ASC;

-- Else if count == 1
SELECT * FROM pictures WHERE altitude>101.71
ORDER BY altitude ASC, time ASC;


--------------------------------------------------------------------------
-- New logic of program
-- Current picture
-- altitude = 98.84
-- time = 1528704751.0
SELECT count(*) FROM pictures WHERE altitude=current_altitude AND time>current_time;

if count == 0
SELECT * FROM pictures WHERE altitude>current_altitude ORDER BY altitude ASC, time ASC;
grab new current_picture

if count > 0
SELECT * FROM pictures WHERE altitude=current_altitude AND time>current_time ORDER BY altitude ASC, time ASC;
grab new current_picture


--------------------------------------------------------------------------
-- Testing
SELECT * FROM pictures WHERE altitude >= 101.71 
ORDER BY
(CASE
	WHEN  count(WHERE altitude > 100) > 15 THEN index_in_hike
	ELSE color
END);

SELECT
CASE 
	WHEN (SELECT count(*) FROM pictures WHERE altitude=101.71) > 1 THEN 
	count(*) FROM pictures WHERE altitude=101.71
END;


--------------------------------------------------------------------------
SELECT count(*) FROM pictures WHERE altitude=101.7 AND time>1528704658.0;

SELECT * FROM pictures WHERE altitude>101.7 ORDER BY altitude ASC, time ASC;

SELECT count(*) FROM pictures WHERE altitude=101.71 AND time>1528704661.0;

SELECT * FROM pictures WHERE altitude=101.71 AND time>1528704663.0 ORDER BY altitude ASC, time ASC;
--------------------------------------------------------------------------
