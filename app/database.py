import time
import pandas as pd
import mysql.connector

def create_tables():

    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="dbmsproject"
    )
    
    c = mydb.cursor(buffered=True)
    with open('/home/sr42/Projects/football-db/databaseSetup.sql', 'r') as f:
        c.execute(f.read(), multi=True)
    c.close()


def add_data(player_id, player_name_surname, position, nationality, player_contract_start_date, player_contract_end_date, age, current_market_value, team_id):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="dbmsproject"
    )
    
    c = mydb.cursor(buffered=True)
    c.execute('INSERT INTO football_player(player_id, player_name_surname, position, nationality, player_contract_start_date, player_contract_end_date, age, current_market_value, team_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)',
              (player_id, player_name_surname, position, nationality, player_contract_start_date, player_contract_end_date, age, current_market_value, team_id))
    mydb.commit()
    c.close()


def view_all_data():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="dbmsproject"
    )
    
    c = mydb.cursor(buffered=True)
    c.execute('SELECT * FROM football_player')
    data = c.fetchall()
    c.close()
    return data


def view_only_dealer_names():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="dbmsproject"
    )
    
    c = mydb.cursor(buffered=True)
    c.execute('SELECT player_name_surname FROM football_player')
    data = c.fetchall()
    c.close()
    return data


def get_dealer(player_name):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="dbmsproject"
    )
    
    c = mydb.cursor(buffered=True)
    c.execute('SELECT * FROM football_player WHERE player_name_surname="{}"'.format(player_name))
    data = c.fetchall()
    c.close()
    return data


def edit_dealer_data(player_id, player_name_surname, position, nationality, player_contract_start_date, player_contract_end_date, age, current_market_value, team_id):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="dbmsproject"
    )
    
    c = mydb.cursor(buffered=True)
    c.execute("UPDATE TRAIN SET player_id=%s, player_name_surname=%s, position=%s, nationality=%s, player_contract_start_date=%s, player_contract_end_date=%s, age=%s, current_market_value=%s, team_id=%s WHERE "
              "player_id=%s, player_name_surname=%s, position=%s, nationality=%s, player_contract_start_date=%s, player_contract_end_date=%s, age=%s, current_market_value=%s, team_id=%s", (player_id, player_name_surname, position, nationality, player_contract_start_date, player_contract_end_date, age, current_market_value, team_id))
    mydb.commit()
    data = c.fetchall()
    c.close()
    return data


def delete_data(player_name):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="dbmsproject"
    )
    
    c = mydb.cursor(buffered=True)
    c.execute('DELETE FROM football_player WHERE player_name_surname="{}"'.format(player_name))
    mydb.commit()
    c.close()


def run_query(query):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="dbmsproject"
    )
    df = pd.read_sql(query, con=mydb)
    return df
