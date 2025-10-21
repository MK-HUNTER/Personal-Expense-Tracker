DB_FILE = 'test'
DB_SCHEMA = '''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            category TEXT NOT NULL,
            amount REAL NOT NULL,
            description TEXT
        )
    '''

CATEGORIES = ['Food', 'Transportation', 'Other']