import pandas as pd
import streamlit as st
from database import view_all_data, view_only_dealer_names, delete_data


def delete():
    result = view_all_data()
    df = pd.DataFrame(result, columns=['league_id', 'league_name', 'country', 'sponsors', 'current_champions', 'top_scorer'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_leagues = [i[0] for i in view_only_dealer_names()]
    selected_league = st.selectbox("League to delete", list_of_leagues)
    st.warning("Are you sure you want to you delete this record :{}".format(selected_league))
    if st.button("Delete league"):  
        delete_data(selected_league)
        st.success("The league has been deleted successfully.")
    new_result = view_all_data()
    df2 = pd.DataFrame(new_result, columns=['league_id', 'league_name', 'country', 'sponsors', 'current_champions', 'top_scorer'])
    with st.expander("Updated data"):
        st.dataframe(df2)