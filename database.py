"""
This module manages all SQLite database operations including:
- Creating and initializing the database
- Adding, retrieving, and deleting expenses
- Clearing all data
"""

import sqlite3
import pandas as pd

# Database Setup Functions

def init_database():
    """
    Initialize the SQLite database and create the expense table if it doesn't exist.
    This function runs once when the app starts. 
    """
    # Connect to database (create file if doesn't exist)
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            category TEXT NOT NULL,
            amount REAL NOT NULL,
            description TEXT
        )
    ''')
    conn.commit() # Save changes
    conn.close()  # Close connection

def add_expense_to_db(date, category, amount, description):
    """Add a new expense to the database.
    Returns True if successful, False otherwise.
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        #Insert new record
        cursor.execute(
            '''
            INSERT INTO expenses (date, category, amount, description)
            VALUE (?, ?, ?, ?)''',
            (str(date), category, amount, description))
        
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        st.error(f"Error adding expese: {e}")
        return False

def get_all_expenses():
    """
    Retrieve all expenses from the database.
    Returns a pandas Dataframe. 
    """

    conn =sqlite3.conn(DB_FILE)

    # Read data into Dataframe
    df = pd.read_sql_query("SELECT * FROM expenses ORDER by date DESC", conn)
    conn.close()

    return df

def delete_expense_from_db(expense_id):
    """
    Delete an expense by its ID. 
    """

    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))

        conn.commit()
        conn.close()
        return True
    except Exception as e:
        st.error(f"Error deleting expense: {e}")
        return False
    
def clear_all_expenses():
    """
    Delete all expenses from the database. 
    """

    try:

        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        cursor.execute("DELETE FROM expenses")
        return True
    except Exception as e:
        st.error(f"Error clearing expenses: {e}")
        return False