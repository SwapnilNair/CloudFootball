import cv2
import pandas as pd
import streamlit as st
from database import run_query, create_tables


def query():

    if st.button("Initialize DB"):
        create_tables()
        st.success("Database successfully populated.")
        
    query = st.text_input('Query')
    if st.button("Run query"):
        result = run_query(query)
        #df = pd.DataFrame(result)
        with st.expander("View all players"):
            st.dataframe(result)

    st.subheader("Database Details :")
    img1 = cv2.imread('graphics/schema.png')
    st.image(img1, caption='Database Schema')

    img2 = cv2.imread('graphics/erd.png')
    st.image(img2, caption='Database Schema')