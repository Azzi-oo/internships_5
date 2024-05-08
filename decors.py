def my_decor(func):
    def wrapper():
        print("Something is happening  before the func is called")
        func()
        print("Something is happening  after the func is called")
    return wrapper

def say_hello():
    print("Hello!")

my_decor(say_hello)()
