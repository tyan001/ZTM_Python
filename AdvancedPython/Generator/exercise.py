# %%
"""
Exercise 1: Basic Generator - Countdown
Create a generator function called 'countdown' that takes a number n and
yields numbers from n down to 1.

Example: list(countdown(5)) should give [5, 4, 3, 2, 1]
"""


def countdown(n):
    
    for i in range(n, 0, -1):
        yield i


# Test your function
print(list(countdown(5)))
# Expected output: [5, 4, 3, 2, 1]

# %%
"""
Exercise 2: Fibonacci Generator
Create a generator function called 'fibonacci' that yields Fibonacci numbers 
indefinitely. The sequence starts with 0, 1, and each subsequent number is 
the sum of the previous two.

You'll need to manually stop it or use islice to get a limited number.
"""


def fibonacci():
    a=0
    b=1
    while True:
        yield a
        temp = a
        a = b
        b = temp + a
    


# Test your function
from itertools import islice
print(list(islice(fibonacci(), 10)))
# Expected output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# %%
"""
Exercise 3: Even Numbers Generator
Create a generator function called 'even_numbers' that takes a start and end 
parameter and yields only even numbers in that range (inclusive of start, 
exclusive of end).

Example: list(even_numbers(1, 10)) should give [2, 4, 6, 8]
"""


def even_numbers(start, end):
    # for i in range(start, end):
    #     if i%2==0:
    #         yield i
    
    if start%2!=0:
        start = start+1
    
    for i in range(start, end,2):
        yield i
    


# Test your function
print(list(even_numbers(1, 10)))
# Expected output: [2, 4, 6, 8]

# %%
"""
Exercise 4: Batch Generator
Create a generator function called 'batch_data' that takes a list and a 
batch_size, and yields the list in batches of the specified size.

Example: list(batch_data([1,2,3,4,5,6,7], 3)) 
         should give [[1,2,3], [4,5,6], [7]]
"""


def batch_data(data, batch_size):
    
    for i in range(0,len(data),batch_size):
        yield data[i:i+batch_size]
    


# Test your function
print(list(batch_data([1,2,3,4,5,6,7], 3)))
# Expected output: [[1, 2, 3], [4, 5, 6], [7]]

# %%
"""
Exercise 5: File Line Reader (Generator Expression)
Create a generator function called 'read_lines' that takes a filename and 
yields each line from the file with whitespace stripped, skipping empty lines.

For testing, first create a sample file.
"""


def read_lines(filename):
    with open(filename, 'r') as f:
        for line in f:
            if line.strip():
                yield line.strip()
        



# Test your function
# First create a test file
with open('test.txt', 'w') as f:
    f.write('Line 1\n\n  Line 2  \nLine 3\n\n')

print(list(read_lines('test.txt')))
# Expected output: ['Line 1', 'Line 2', 'Line 3']

# %%
"""
Exercise 6: Infinite Cycle Generator
Create a generator function called 'cycle' that takes an iterable and 
yields its elements indefinitely in a cycle.

Example: The first 8 elements of cycle([1,2,3]) should be [1,2,3,1,2,3,1,2]
"""


# def cycle(iterable):
#     i=0
#     while True:
#        yield iterable[i]
#        i += 1
#        if i==len(iterable): 
#            i=0
    
def cycle(iterable):
    saved = list(iterable)
    while True:
        yield from saved


# Test your function
# from itertools import islice
print(list(islice(cycle([1, 2, 3]), 8)))
print(list(islice(cycle("hello"), 8)))
# Expected output: [1, 2, 3, 1, 2, 3, 1, 2]

# %%
"""
Exercise 7: Prime Numbers Generator
Create a generator function called 'primes' that yields prime numbers 
indefinitely starting from 2.

Use a simple trial division method.
"""


def primes():
    
    
    
    pass


# Test your function
# from itertools import islice
# print(list(islice(primes(), 10)))
# Expected output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

# %%
"""
Exercise 8: Generator with send() - Running Average
Create a generator function called 'running_average' that maintains a 
running average. It should yield None initially, then accept numbers via 
send() and yield the current average after each number.

This uses the advanced .send() method of generators.
"""


def running_average():
    pass


# Test your function
# avg = running_average()
# next(avg)  # Prime the generator
# print(avg.send(10))  # Expected: 10.0
# print(avg.send(20))  # Expected: 15.0
# print(avg.send(30))  # Expected: 20.0

# %%
"""
Exercise 9: Flatten Nested Lists
Create a generator function called 'flatten' that takes a nested list 
(lists within lists, any depth) and yields all elements in a flat sequence.

Example: list(flatten([1, [2, 3], [[4], 5]])) should give [1, 2, 3, 4, 5]
"""


def flatten(nested_list):
    pass


# Test your function
# print(list(flatten([1, [2, 3], [[4], 5]])))
# Expected output: [1, 2, 3, 4, 5]

# %%
"""
Exercise 10: Generator Pipeline
Create three generator functions that work together:
1. 'numbers(n)' - yields numbers from 1 to n
2. 'square(gen)' - takes a generator and yields squared values
3. 'filter_even(gen)' - takes a generator and yields only even values

Chain them together to get squared even numbers.
"""


def numbers(n):
    pass


def square(gen):
    pass


def filter_even(gen):
    pass


# Test your functions
# result = filter_even(square(numbers(10)))
# print(list(result))
# Expected output: [4, 16, 36, 64, 100]
