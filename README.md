# football-database
A streamlit/mysql based web-application to manipulate a database of football players.

### Setup & execution instructions (Ubuntu 20.04) :

1. Clone this repository into any location of your choice.
2. Open the terminal and navigate to the directory where you cloned the repository.
3. Run the following command (in your virtual environment if you're using one) to install the required dependencies :

    ```pip install -r requirements.txt```
4. Change the .sql file paths in 'databaseSetup.sql'.
5. Install and set up the mysql server package as per the instructions on https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04
6. Create a database by the name of 'dbmsproject' and use it.
5. Run the following command in the 'app' directory to start the streamlit server :

    ```streamlit run app.py```


### Reference : https://github.com/Ojjie/Sem4-Assignments/tree/master/DBMS/Final%20project%20
