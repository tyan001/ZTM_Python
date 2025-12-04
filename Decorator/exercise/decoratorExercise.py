# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
# %%
user1 = {
    "name": "Sorna",
    "valid": True,  # changing this will either run or not run the message_friends function.
}


def authenticated(fn):
    def wrapper(*args, **kwargs):
        if args[0]["valid"]:
            return fn(*args, **kwargs)
        else:
            return f"invalid user"

    return wrapper


@authenticated
def message_friends(user):
    print("message has been sent")


message_friends(user1)
# --------------------------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------------------


# %%
# A decorator is just a function that takes a function and returns a new function
def my_decorator(func):
    def wrapper(
        *args, **kwargs
    ):  # *args catches positional args, **kwargs catches keyword args
        print("Something happens before")
        result = func(
            *args, **kwargs
        )  # Call the original function with whatever args it received
        print("Something happens after")
        return result  # Don't forget to return the result!

    return wrapper


# Using the @ syntax is just shorthand for: greet = my_decorator(greet)
@my_decorator
def greet(name):
    print(f"Hello, {name}!")


greet("Alice")
# Output:
# Something happens before
# Hello, Alice!
# Something happens after
# %%
# A practical example: timing how long a function takes
import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()  # Record start time
        result = func(*args, **kwargs)  # Run the actual function
        end = time.time()  # Record end time
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result

    return wrapper


@timer
def slow_add(a, b):
    time.sleep(0.5)  # Simulate slow operation
    return a + b


@timer
def slow_multiply(x, y, z):  # Works with any number of parameters!
    time.sleep(0.3)
    return x * y * z


print(slow_add(2, 3))  # Works with 2 args
print(slow_multiply(2, 3, 4))  # Works with 3 args


# %%
# Why *args, **kwargs matters: it makes decorators flexible
def debug(func):
    def wrapper(*args, **kwargs):
        # We can inspect what was passed in
        print(f"Calling {func.__name__}")
        print(f"  Positional args: {args}")  # Tuple of positional arguments
        print(f"  Keyword args: {kwargs}")  # Dict of keyword arguments
        print(f"  {func(*args, **kwargs)}")
        return func(*args, **kwargs)

    return wrapper


@debug
def make_greeting(name, greeting="Hello", punctuation="!"):
    return f"{greeting}, {name}{punctuation}"


# All these work with the same decorator:
make_greeting("Bob")  # args=('Bob',), kwargs={}
make_greeting("Bob", "Hi")  # args=('Bob', 'Hi'), kwargs={}
make_greeting("Bob", punctuation="?")  # args=('Bob',), kwargs={'punctuation': '?'}
make_greeting(
    name="Bob", greeting="Hey"
)  # args=(), kwargs={'name': 'Bob', 'greeting': 'Hey'}
# %%
# Exercise 1: Call Counter
# Create a decorator that counts how many times a function has been called.
# Hint: You can store the count as an attribute on the wrapper function itself.

# Your code here

def call_counter(fn):
    def wrapper(*args, **kwargs):  # 2. This DEFINES wrapper, doesn't run it yet
        wrapper.count += 1
        return fn(*args, **kwargs)

    wrapper.count = 0  # 3. This runs ONCE, right after wrapper is defined
    return wrapper  # 4. Return the wrapper (with .count already set to 0)


@call_counter  # 1. This calls call_counter(say_hello) ONE time
def say_hello(name):
    return f"Hello, {name}!"


# Test it:
print(say_hello("Alice"))    # Hello, Alice!
print(say_hello("Bob"))      # Hello, Bob!
print(say_hello("Charlie"))  # Hello, Charlie!
print(say_hello.count)       # Expected: 3

# %%
# Exercise 2: Argument Validator
# Create a decorator that prints a warning if any argument is None.
# The function should still run normally.

# Your code here
def warn_none(fn):
    def wrapper(*args,**kwargs):
        for i,arg in enumerate(args):
            if arg is None:
                print(f"Warning: argument at position {i} is None")
        for key,value in kwargs.items():
            if value is None:
                print(f"Warning: keyword argument {key} at position is None")
        return fn(*args, **kwargs)
    return wrapper

@warn_none
def create_user(username, email, age=None):
    return {"username": username, "email": email, "age": age}


# Test it:
create_user("alice", "alice@example.com", age=25)
# Expected output: (no warning, just returns the dict)

create_user("bob", None, age=30)
# # Expected output: "Warning: argument at position 1 is None"

create_user("charlie", "c@example.com", age=None)
# # Expected output: "Warning: keyword argument 'age' is None"

# %%
# Exercise 3: Retry Decorator
# Create a decorator that retries a function up to 3 times if it raises an exception.
# Print which attempt number it's on.

# Your code here


import random
def retry(fn):
    def wrapper(*args,**kwargs):
        for attempt in range(1,4):
            try:
                return fn(*args, **kwargs)
            except Exception as e:
                print(f"attempt number {attempt}")
                print(e)
                if attempt ==3:
                    print(f'3 attemps are used')
                    return -1
    
    return wrapper

@retry
def unreliable_function():
    if random.random() < 0.7:  # 70% chance of failure
        raise ValueError("Random failure!")
    return "Success!"


# Test it multiple times:
print(unreliable_function())
# Expected output (varies):
# Attempt 1 failed: Random failure!
# Attempt 2 failed: Random failure!
# Attempt 3: Success!
# "Success!"

# %%
# Exercise 4: Before and After Hooks
# Create a decorator that accepts two optional functions: one to run before
# and one to run after the decorated function.
# Hint: This requires a decorator that takes arguments (decorator factory).

# Your code here
def with_hooks(before=None, after=None):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            if before:
                before()
            result = fn(*args, **kwargs)
            if after:
                after()
            return result

        return wrapper

    return decorator



def before_hook():
    print(">> Starting operation...")


def after_hook():
    print(">> Operation complete!")


@with_hooks(before=before_hook, after=after_hook)
def process_data(data):
    print(f"Processing: {data}")
    return data.upper()


# Test it:
result = process_data("hello world")
# Expected output:
# >> Starting operation...
# Processing: hello world
# >> Operation complete!
# print(result)  # "HELLO WORLD"

# %%
