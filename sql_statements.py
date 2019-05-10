# Holds all SQL statements for the program


class SQLStatements:

    # Select by ID and index
    def select_by_ids_picture(self, hike_id: int, index_in_hike: int) -> str:
        statement = 'SELECT * FROM pictures WHERE hike={id} AND \
            index_in_hike={index}'.format(id=hike_id, index=index_in_hike)
        return statement

    # Time across Hikes
    def select_by_time_first_picture(self) -> str:
        statement = 'SELECT * FROM pictures ORDER BY time ASC LIMIT 1'
        return statement

    def select_by_time_last_picture(self) -> str:
        statement = 'SELECT * FROM pictures ORDER BY time DESC LIMIT 1'
        return statement

    # def select_by_time_next_picture() -> str:

    # def select_by_time_previous_picture() -> str:

    # Altitude - greatest & least across hikes
    def select_by_altitude_greatest_picture(self) -> str:
        statement = 'SELECT * FROM pictures ORDER BY altitude DESC LIMIT 1'
        return statement

    def select_by_altitude_least_picture(self) -> str:
        statement = 'SELECT * FROM pictures ORDER BY altitude ASC LIMIT 1'
        return statement

    # Altitude - count of same altitude across hikes
    def find_size_by_altitude_greater_time(self, altitude: float, time: float) -> str:
        statement = 'SELECT count(*) FROM pictures WHERE altitude={alt} \
            AND time>{t}'.format(alt=altitude, t=time)
        return statement

    def find_size_by_altitude_less_time(self, altitude: float, time: float) -> str:
        statement = 'SELECT count(*) FROM pictures WHERE altitude={alt} \
            AND time<{t}'.format(alt=altitude, t=time)
        return statement

    # Altitude - next across hikes
    def select_by_greater_altitude_next_picture(self, altitude: float) -> str:
        statement = 'SELECT * FROM pictures WHERE altitude>{alt} \
            ORDER BY altitude ASC, time ASC LIMIT 1'.format(alt=altitude)
        return statement

    def select_by_equal_altitude_next_picture(self, altitude: float, time: float) -> str:
        statement = 'SELECT * FROM pictures WHERE altitude={alt} AND \
            time>{t} ORDER BY altitude ASC, time ASC LIMIT 1'.format(alt=altitude, t=time)
        return statement

    # Altitude - previous across hikes
    def select_by_less_altitude_previous_picture(self, altitude: float) -> str:
        statement = 'SELECT * FROM pictures WHERE altitude<{alt} \
            ORDER BY altitude DESC, time DESC'.format(alt=altitude)
        return statement

    def select_by_equal_altitude_previous_picture(self, altitude: float, time: float) -> str:
        statement = 'SELECT * FROM pictures WHERE altitude={alt} AND \
            time<{t} ORDER BY altitude DESC, time DESC'.format(alt=altitude, t=time)
        return statement

    # Next and Previous Altitude in Hike
    # def select_next

    # Color
    # def select_by_color_next_picture() -> str:

    # def select_by_color_previous_picture() -> str:
