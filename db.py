import psycopg2

db_name = "bet_365"
db_user = "bet_365_admin"
db_user_password = "bet365admin"

def create_connection(db_name, db_user, db_user_password):
    connection = psycopg2.connect(database=db_name, user=db_user, password=db_user_password)
    return connection

def create_tables(connection):
    user_table = "CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, name TEXT NOT NULL)"
    item_table = "CREATE TABLE IF NOT EXISTS items (id SERIAL PRIMARY KEY, name TEXT NOT NULL)"
    order_table = "CREATE TABLE IF NOT EXISTS orders (id SERIAL PRIMARY KEY, user_id INT, item_id INT, CONSTRAINT fk_item FOREIGN KEY (item_id) REFERENCES items(id), CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES users(id))"

    cursor = connection.cursor()
    
    cursor.execute(user_table)
    cursor.execute(item_table)
    cursor.execute(order_table)
    connection.commit()


if __name__ == "__main__":
    connection = create_connection(db_name, db_user, db_user_password)
    create_tables(connection)