import db
import cProfile

def create_tables(connection):
    what = "CREATE TABLE IF NOT EXISTS what (id SERIAL PRIMARY KEY, userz TEXT NOT NULL, item TEXT NOT NULL, order_date DATE)"

    cursor = connection.cursor()

    cursor.execute(what)
    connection.commit()

def insert_row(user, item, date, cursor):
    cursor.execute(f"INSERT INTO what(userz, item, order_date) VALUES ('{user}', '{item}', '{date}')")
    

def main():
    c1 = db.default_connection()
    create_tables(c1)
    with open("customer_orders.csv", "r") as f:
        con = db.default_connection()
        cur = con.cursor()
        for line_number, line in enumerate(f):
            if line_number % 10000 == 0:
                print("here")
                con.commit()            
            user, item, date = line.split(",")
            cur.execute(f"INSERT INTO what(userz, item, order_date) VALUES ('{user[1:-1]}', '{item[1:-1]}', '{date[1:-1]}')")
        con.commit()

if __name__ == "__main__":
    c1 = db.default_connection()
    create_tables(c1)