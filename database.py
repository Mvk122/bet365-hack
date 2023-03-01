<<<<<<< HEAD
from pymongo import MongoClient
import creds 

class MongoDatabase:

   def __init__(self, url):
      self.db = self.get_database(url)

   def get_database(self, url):
      CONNECTION_STRING = url
      client = MongoClient(CONNECTION_STRING)
        
      return client['Bet365']

   def create_collection(self):
      self.transactions = self.db["transactions"]

   def insert_transaction(self, transaction)
      self.transactions.insert_many(transaction)

if __name__ == "__main__":   
   db = MongoDatabase(creds.db_url)
   with open("customer_orders.csv", "r") as f:
        for line_number, line in enumerate(f):
            if line_number % 10000 == 0:
               print("here")           
            user, item, date = line.split(",")
            transaction = {
               "user" : user,
               "item" : item,
               "date": date,
            }

            db.insert_transaction(transaction)
=======
from pymongo import MongoClient
import creds 

class MongoDatabase:

   def __init__(self, url):
      self.db = self.get_database(url)

   def get_database(self, url):
        CONNECTION_STRING = url
        client = MongoClient(CONNECTION_STRING)
        
        return client['Bet365']

   def create_collection(self):
        self.transactions = self.db["transactions"]

   def insert_transaction(self, transaction_url):


if __name__ == "__main__":   
    db = MongoDatabase(creds.db_url)
    db.insert_transaction()
>>>>>>> 4e0b85c (add mongo script)
