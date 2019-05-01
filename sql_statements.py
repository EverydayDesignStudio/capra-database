# Holds all SQL statements for the program


class SQLStatements:
    # def __init__(self):

    def select_photo(self, hike_id, index_in_hike) -> str:
        select_statement = 'SELECT * FROM pictures WHERE hike={id} AND \
            index_in_hike={index}'.format(id=hike_id, index=index_in_hike)
        return select_statement
