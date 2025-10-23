"""
This module contains all configuration settings and constants
"""

# Expense categories
EXPENSE_CATEGORIES = [
    'Food',
    'Transportation',
    'Entertainment',
    'Shopping',
    'Bills',
    'Healthcare',
    'Education',
    'Other'
]

# Database settings
DATABASE_NAME = 'expenses.db'

# Page configuration
PAGE_CONFIG = {
    'page_title': 'Expense Tracker',
    'page_icon': '💰',
    'layout': 'wide'
}

# Column names (for consistency across modules)
COLUMN_NAMES = {
    'id': 'id',
    'date': 'date',
    'category': 'category',
    'amount': 'amount',
    'description': 'description'
}