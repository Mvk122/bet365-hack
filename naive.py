import db

def get_user_id(user, connection):
    # TODO make this use the cache
    cursor = connection.cursor()
    cursor.execute(f"select id from users where name='{user}'")
    record = cursor.fetchall()
    if len(record == 0):
        return False
    else:
        return record[0][0]

def get_item_id(item, connection):
    # TODO make this use the cache
    cursor = connection.cursor()
    cursor.execute(f"select id from items where name='{item}'")
    record = cursor.fetchall()
    if len(record == 0):
        return False
    else:
        return record[0][0]

def create_user(username, connection)-> int:
    connection.cursor().execute(f"INSERT INTO users(name) VALUES ('{username}')")
    connection.commit()
    return get_user_id(username, connection)

def create_item(item, connection):
    connection.cursor().execute(f"INSERT INTO items(name) VALUES ('{item}')")
    connection.commit()
    return get_item_id(item, connection)

def create_transaction(item_id, user_id, connection):
    connection.cursor().execute(f"INSERT INTO orders(user_id, item_id) VALUES ({user_id}, {item_id})")
    connection.commit()

def insert_row(user, item, date, connection):
    user_id = get_user_id(user, connection)
    if type(user_id) != int:
        user_id = create_user(user)
    
    item_id = get_item_id(item, connection)
    if type(item_id) != int:
        item_id = create_item(item)

    

