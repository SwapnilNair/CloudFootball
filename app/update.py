import pandas as pd
import streamlit as st
from database import view_all_data, view_only_dealer_names, get_dealer, edit_dealer_data


def update():
    result = view_all_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=['player_id', 'player_name_surname', 'position', 'nationality', 'player_contract_start_date', 'player_contract_end_date', 'age', 'current_market_value', 'team_id'])
    with st.expander("Players in roster :"):
        st.dataframe(df)
    list_of_players = [i[0] for i in view_only_dealer_names()]
    selected_players = st.selectbox("Players to edit", list_of_players)
    selected_result = get_dealer(selected_players)
    # st.write(selected_result)
    
    if selected_result:
        player_id, player_name_surname, position, nationality, player_contract_start_date, player_contract_end_date, age, current_market_value, team_id = selected_result[0][0], selected_result[0][1], selected_result[0][2], selected_result[0][3], selected_result[0][4], selected_result[0][5], selected_result[0][6], selected_result[0][7], selected_result[0][8]

        # Layout of Create
        
        col1, col2 = st.columns(2)

        '''
        with col1:
            new_Train_id = st.text_input("ID:", Train_id)
            new_Train_name = st.text_input("Name:", Train_name)
        with col2:
            new_Train_type = st.selectbox(Train_type, ["Superfast", "Fast", "Mail"])
            new_Source = st.text_input("Source:", Source)
        new_Destination = st.text_input("Destination:", Destination)
        new_Availability = st.text_input("Availability:", Availability)
        '''

        with col1:
            player_id = st.text_input('Player ID', player_id)
            player_name_surname = st.text_input("Player Name", player_name_surname)
            position = st.selectbox("Type: ", ["Forward", "Midfield", "Defender", "Goalkeeper"])
            nationality = st.text_input("Nationality", nationality)

        with col2:
            player_contract_start_date = st.text_input("Contract Start Date (YYYY-MM-DD)", player_contract_start_date)
            player_contract_end_date = st.text_input("Contract End Date (YYYY-MM-DD)", player_contract_end_date)
            age = st.text_input('Age', age)
            current_market_value = st.text_input("Current Market Value (In Millions of USD)", current_market_value)
            
        team_id = st.text_input('Team ID', team_id)

        if st.button("Update Player"):
            edit_dealer_data(player_id, player_name_surname, position, nationality, player_contract_start_date, player_contract_end_date, age, current_market_value, team_id)
            st.success("Successfully updated record")

    result2 = view_all_data()
    df2 = pd.DataFrame(result2, columns=['player_id', 'player_name_surname', 'position', 'nationality', 'player_contract_start_date', 'player_contract_end_date', 'age', 'current_market_value', 'team_id'])
    with st.expander("Updated data"):
        st.dataframe(df2)
