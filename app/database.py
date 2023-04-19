import time
import pandas as pd
import mysql.connector


def create_tables():

    mydb = mysql.connector.connect(
        host="database-1.clvmopeeygko.ap-south-1.rds.amazonaws.com",
        user="admin",
        password="admin123",
        database="dbmsproject"
    )

    c = mydb.cursor(buffered=True)
    with open('~/football-db/databaseSetup.sql', 'r') as f:
        c.execute(f.read(), multi=True)
    c.close()


def add_data(league_id, league_name, country, sponsors, current_champions, top_scorer):
    mydb = mysql.connector.connect(
        host="database-1.clvmopeeygko.ap-south-1.rds.amazonaws.com",
        user="admin",
        password="admin123",
        database="dbmsproject"
    )

    c = mydb.cursor(buffered=True)
    c.execute('INSERT INTO league(league_id, league_name, country, sponsors, current_champions, top_scorer) VALUES (%s,%s,%s,%s,%s,%s)',
              (league_id, league_name, country, sponsors, current_champions, top_scorer))
    mydb.commit()
    c.close()


def view_all_data():
    mydb = mysql.connector.connect(
        host="database-1.clvmopeeygko.ap-south-1.rds.amazonaws.com",
        user="admin",
        password="admin123",
        database="dbmsproject"
    )

    c = mydb.cursor(buffered=True)
    c.execute('SELECT * FROM league')
    data = c.fetchall()
    c.close()
    return data


def view_only_dealer_names():
    mydb = mysql.connector.connect(
        host="database-1.clvmopeeygko.ap-south-1.rds.amazonaws.com",
        user="admin",
        password="admin123",
        database="dbmsproject"
    )

    c = mydb.cursor(buffered=True)
    c.execute('SELECT league_name FROM league')
    data = c.fetchall()
    c.close()
    return data


def get_dealer(league_name):
    mydb = mysql.connector.connect(
        host="database-1.clvmopeeygko.ap-south-1.rds.amazonaws.com",
        user="admin",
        password="admin123",
        database="dbmsproject"
    )

    c = mydb.cursor(buffered=True)
    c.execute('SELECT * FROM league WHERE league_name="{}"'.format(league_name))
    data = c.fetchall()
    c.close()
    return data


def edit_dealer_data(league_id, league_name, country, sponsors, current_champions, top_scorer, league_id1, league_name1, country1, sponsors1, current_champions1, top_scorer1):
    mydb = mysql.connector.connect(
        host="database-1.clvmopeeygko.ap-south-1.rds.amazonaws.com",
        user="admin",
        password="admin123",
        database="dbmsproject"
    )

    c = mydb.cursor(buffered=True)
    c.execute("UPDATE league SET league_id=%s, league_name=%s, country=%s, sponsors=%s, current_champions=%s, top_scorer=%s WHERE league_id=%s",
              (league_id1, league_name1, country1, sponsors1, current_champions1, top_scorer1, league_id))
    mydb.commit()
    c.close()


def delete_data(league_name):
    mydb = mysql.connector.connect(
        host="database-1.clvmopeeygko.ap-south-1.rds.amazonaws.com",
        user="admin",
        password="admin123",
        database="dbmsproject"
    )

    c = mydb.cursor(buffered=True)
    c.execute('DELETE FROM league WHERE league_name="{}"'.format(league_name))
    mydb.commit()
    c.close()


def run_query(query):
    mydb = mysql.connector.connect(
        host="database-1.clvmopeeygko.ap-south-1.rds.amazonaws.com",
        user="admin",
        password="admin123",
        database="dbmsproject"
    )
    df = pd.read_sql(query, con=mydb)
    return df
