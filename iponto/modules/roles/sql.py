class SQLRole:
    _TABLE_NAME = 'roles'
    _COL_ID = 'id'
    _COL_TITLE = 'title'

    _CREATE_TABLE = (f'CREATE TABLE IF NOT EXISTS {_TABLE_NAME}'
                     f'({_COL_ID} SERIAL PRIMARY KEY,'
                     f'{_COL_TITLE} VARCHAR(255) unique);')

    _INSERT_ROLE = f'INSERT INTO {_TABLE_NAME}({_COL_TITLE}) values %s'
    _SELECT_ALL = f"SELECT * from {_TABLE_NAME}"
    _SELECT_BY_ID = f'SELECT * from {_TABLE_NAME} WHERE {_COL_ID} = %s'

    @property
    def CREATE_TABLE(self):
        return self._CREATE_TABLE