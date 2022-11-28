# Importing pakages
import streamlit as st
import mysql.connector

from create import create
from database import create_tables
from delete import delete
from read import read
from update import update
from query import query


def main():
    st.title("⚽ Fußball Datenbank")
    menu = ["Initialize & Query" ,"Add", "Delete", "Update", "View"]
    choice = st.sidebar.selectbox("Operations", menu)

    create_tables()

    if choice == "Add":
        st.subheader("Input Player Details")
        create()

    elif choice == "View":
        st.subheader("View Player Roster")
        read()

    elif choice == "Update":
        st.subheader("Update Player Roster")
        update()

    elif choice == "Delete":
        st.subheader("Delete Player Records")
        delete()

    elif choice == "Initialize & Query":
        st.subheader("Initialize & Query")
        query()

    else:
        st.subheader("Lorem ipsum")


if __name__ == '__main__':
    main()
