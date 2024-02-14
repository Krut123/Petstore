def greet(fx):
    def modified(*args):
        print("good morning")
        fx()
        print("thank you")
    return modified;

@greet 
def hello():
    print("hello world")

hello()


def pretty(func):
    def inner():
        print("i got decorated")
        func()
        print("end")
    return inner

@pretty
def ordinary():
    print("i am ordinary")

ordinary()

