# Import necessary libraries
import streamlit as st
import pandas as pd
from datetime import datetime
from config import CATEGORIES

st.set_page_config(
    page_title="Expense Tracker",
    page_icon = "💰",
    layout= "wide"
)

st.title("💰 Personal Expense Tracker")
st.markdown("*Connected to SQLite Database* 🗄️")
st.markdown("----")

#Create sidebar for adding expenses
with st.sidebar:
    st.header("Add New Expense")

    with st.form("expense_form"):
        expense_data = st.date_input("Date", datetime.now())
        category = st.selectbox("Category", CATEGORIES)
        amount = st.number_input("Amount", min_value=0.0, step =0.05, format="%.2f")
        description = st.text_input("Description")

        submitted = st.form_submit_button("Add Expense")