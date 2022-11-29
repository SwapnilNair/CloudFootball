import streamlit as st
from database import add_data

# league_id, league_name, country, sponsors, current_champions, top_scorer

def create():
    col1, col2 = st.columns(2)

    with col1:
        league_id = st.text_input('League ID')
        league_name = st.text_input("League Name")
        country = st.text_input("Country of Origin")

    with col2:
        sponsor = st.text_input("Primary Sponsor")
        current_champion = st.text_input("Current Champion (Team)")
        top_scorer = st.text_input('Top Scorer (Player)')

    if st.button("Commit to Database"):
        add_data(league_id, league_name, country, sponsor, current_champion, top_scorer)
        st.success("Successfully added League: {}".format(league_name))
