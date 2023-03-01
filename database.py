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
