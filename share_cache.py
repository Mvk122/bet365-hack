import redis

# create a Redis client instance
r = redis.Redis(host='localhost', port=6379, db=0)

if r.ping():
    print("PONG")
else:
    print("Connection failed!")
    exit(1)

# set a key-value pair
# r.set('key', 'value')

# get a value by key
value = r.get('key')
print(value)




# @cache.cache(10,60)
# def my_func(arg1, arg2):
#     for i in range (100000):
#         continue
#     result = 10
#     return result

# # Use the function
# t1 = time.time()
# my_func(1, 2)
# print(time.time() - t1)

# # Call it again with the same arguments and it will use cache
# t2= time.time()
# my_func(1, 2)
# print(time.time() - t2)

# # Invalidate a single value
# # my_func.invalidate(1, 2)

# # Invalidate all values for function
# # my_func.invalidate_all()