import streamlit as st
from database import add_data

# player_id, player_name_surname, position, nationality, player_contract_start_date, player_contract_end_date, age, current_market_value, team_id
# (%d,%s,%s,%s,%s,%s,%d,%f,%d)

def create():
    col1, col2 = st.columns(2)

    with col1:
        player_id = st.text_input('Player ID')
        player_name_surname = st.text_input("Player Name")
        position = st.selectbox("Type: ", ["Forward", "Midfield", "Defender", "Goalkeeper"])
        nationality = st.text_input("Nationality")

    with col2:
        player_contract_start_date = st.text_input("Contract Start Date (YYYY-MM-DD)")
        player_contract_end_date = st.text_input("Contract End Date (YYYY-MM-DD)")
        age = st.text_input('Age')
        current_market_value = st.text_input("Current Market Value (In Millions of USD)")

    team_id = st.text_input('Team ID')

    if st.button("Commit to Database"):
        add_data(player_id, player_name_surname, position, nationality, player_contract_start_date, player_contract_end_date, age, current_market_value, team_id)
        st.success("Successfully added player: {}".format(player_name_surname))
