def my_decorator(func):
    def wrapper():
        print("hi, print before executing the function")
        func()
    
    return wrapper

@my_decorator
def hello():
    print("hello hello")

hello()