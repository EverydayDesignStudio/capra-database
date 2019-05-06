# Holds all SQL statements for the program


class SQLStatements:

    # Select by ID and index
    def select_picture(self, hike_id: int, index_in_hike: int) -> str:
        select_statement = 'SELECT * FROM pictures WHERE hike={id} AND \
            index_in_hike={index}'.format(id=hike_id, index=index_in_hike)
        return select_statement

    # time
    def selct_by_time_first_picture(self) -> str:
        select_statement = 'SELECT * FROM pictures ORDER BY time ASC \
            LIMIT 1'
        return select_statement

    def selct_by_time_last_picture(self) -> str:
        select_statement = 'SELECT * FROM pictures ORDER BY time DESC \
            LIMIT 1'
        return select_statement

    # def select_by_time_next_picture() -> str:

    # def select_by_time_previous_picture() -> str:

    # altitude
    def find_size_by_altitude(self, altitude: float, time: float) -> str:
        select_statement = 'SELECT count(*) FROM pictures WHERE altitude={alt} \
            AND time>{t}'.format(alt=altitude, t=time)
        return select_statement

    def select_by_greater_altitude_next_picture(self, altitude: float) -> str:
        select_statement = 'SELECT * FROM pictures WHERE altitude>{alt} \
            ORDER BY altitude ASC, time ASC LIMIT 1'.format(alt=altitude)
        return select_statement

    def select_by_equal_altitude_next_picture(self, altitude: float, time: float) -> str:
        select_statement = 'SELECT * FROM pictures WHERE altitude={alt} AND \
            time>{t} ORDER BY altitude ASC, time ASC LIMIT 1'.format(alt=altitude, t=time)
        return select_statement

    # def select_by_altitude_previous_picture() -> str:

    # color
    # def select_by_color_next_picture() -> str:

    # def select_by_color_previous_picture() -> str:
