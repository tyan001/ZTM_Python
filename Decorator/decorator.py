#%%

def hello():
    print("Hellooooooooooooooooo")
    
# greet = hello()
greet = hello

# print(greet)
print(greet())
# %%
def hello(func):
    func()
    
def greet():
    print('still here!')
    
a = hello(greet)

print(a)

# %%

def my_decorator(func):
    def wrapper():
        print('*************')
        func()
        print("*************")
    return wrapper

@my_decorator
def hello():
    print("hello")
    
hello()
# %%
def my_decorator(func):
    def wrapper(greeting, emoji):
        print("*************")
        func(greeting, emoji)
        print("*************")

    return wrapper


@my_decorator
def hello(greeting, emoji):
    print(greeting, emoji)
    

hello('hi', ':)')
# %%
# %%
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("*************")
        func(*args, **kwargs)
        print("*************")

    return wrapper


@my_decorator
def hello(greeting, emoji=':)'):
    print(greeting, emoji)


hello('hiiii')
# %%
from time import time

def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'took {t2-t1} s')
        return result
    return wrapper

@performance
def long_time():
    for i in range(1000000):
        i*5

long_time()

# %%
