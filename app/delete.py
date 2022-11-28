import pandas as pd
import streamlit as st
from database import view_all_data, view_only_dealer_names, delete_data


def delete():
    result = view_all_data()
    df = pd.DataFrame(result, columns=['player_id', 'player_name_surname', 'position', 'nationality', 'player_contract_start_date', 'player_contract_end_date', 'age', 'current_market_value', 'team_id'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_players = [i[0] for i in view_only_dealer_names()]
    selected_player = st.selectbox("Player to delete", list_of_players)
    st.warning("Are you sure you want to you delete this record :{}".format(selected_player))
    if st.button("Delete player"):
        delete_data(selected_player)
        st.success("The player has been deleted successfully.")
    new_result = view_all_data()
    df2 = pd.DataFrame(new_result, columns=['player_id', 'player_name_surname', 'position', 'nationality', 'player_contract_start_date', 'player_contract_end_date', 'age', 'current_market_value', 'team_id'])
    with st.expander("Updated data : "):
        st.dataframe(df2)