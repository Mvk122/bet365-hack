import db
import cProfile

users = {}
items = {}

def get_user_id(user, connection):
    # TODO make this use the cache
    if user in users:
        return users[user]
    cursor = connection.cursor()
    cursor.execute(f"select id from users where name='{user}'")
    record = cursor.fetchall()
    cursor.close()
    if len(record) ==0:
        return False
    else:
        users[user] = record[0][0]
        return record[0][0]

def get_item_id(item, connection):
    # TODO make this use the cache
    if item in items:
        return items[item]
    cursor = connection.cursor()
    cursor.execute(f"select id from items where name='{item}'")
    record = cursor.fetchall()
    cursor.close()
    if len(record) == 0:
        return False
    else:
        items[item] = record[0][0]
        return record[0][0]

def create_user(username, connection)-> int:
    cur = connection.cursor()
    cur.execute(f"INSERT INTO users(name) VALUES ('{username}')")
    cur.close()
    connection.commit()
    return get_user_id(username, connection)

def create_item(item, connection):
    cur = connection.cursor()
    cur.execute(f"INSERT INTO items(name) VALUES ('{item}')")
    cur.close()
    connection.commit()
    return get_item_id(item, connection)

def create_transaction(item_id, user_id, order_date, cursor):
    cursor.execute(f"INSERT INTO orders(user_id, item_id, order_date) VALUES ({user_id}, {item_id}, '{order_date}')")

def insert_row(user, item, date, connection, cursor):
    user_id = get_user_id(user, connection)
    if type(user_id) != int:
        user_id = create_user(user, connection)
    
    item_id = get_item_id(item, connection)
    if type(item_id) != int:
        item_id = create_item(item, connection)

    create_transaction(item_id, user_id, date, cursor)

def main():
    with open("customer_orders.csv", "r") as f:
        con = db.default_connection()
        cur = con.cursor()
        for line_number, line in enumerate(f):
            if line_number == 200:
                break
            user, item, date = line.split(",")
            insert_row(user[1:-1], item[1:-1], date[1:-1], db.default_connection(), cur)
        cur.commit()

if __name__ == "__main__":
    cProfile.run("main()")


    

