import redis


class lru_cache:
    def __init__(self, db=0):
        # create a Redis client instance
        self.r = redis.Redis(host='localhost', port=6379, db=db)
        self.check_connection()

    def check_connection(self):
        if not self.r.ping():
            print("Connection failed!")
            exit(1)

    def get(self, name):
        return self.r.get(name).decode("utf-8")

    def set(self, name, id):
        self.r.mset({name:id})
    
    def keys(self):
        return self.r.keys()
