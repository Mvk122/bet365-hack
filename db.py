import psycopg2

db_name = "bet_365"
db_user = "bet_365_admin"
db_user_password = "bet365admin"

def create_connection(db_name, db_user, db_user_password):
    connection = psycopg2.connect(database=db_name, user=db_user, password=db_user_password)
    return connection.cursor()

def create_tables(cursor):
    user_table = "CREATE TABLE users (id SERIAL PRIMARY KEY, name TEXT NOT NULL)"
    cursor.execute(user_table)

if __name__ == "__main__":
    connection = create_connection(db_name, db_user, db_user_password)
    create_tables(connection)