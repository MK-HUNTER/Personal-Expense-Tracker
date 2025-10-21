import streamlit as st
import os
import sqlite3 # For database operations
from config import DB_FILE, DB_SCHEMA

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
    Rerurns True if successful, False otherwise.
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
