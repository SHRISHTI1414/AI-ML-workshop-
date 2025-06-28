def my_decorator(func):
    def wrapper():
        print("before the function runs...")
        func()
        print("after the function runs....")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")
    
say_hello()
