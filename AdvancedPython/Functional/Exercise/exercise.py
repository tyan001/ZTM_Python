"""
Python Functional Programming Exercises
Functions: map(), filter(), zip(), reduce()
Modern Python (2020-2025)

Instructions:
- Solve each exercise using the specified function
- Try to use lambda functions where appropriate
- Test your solutions with the provided test cases
"""
# %%
from functools import reduce
from typing import List, Tuple, Dict

# =============================================================================
# MAP EXERCISES
# =============================================================================

#%%
def exercise_1_map():
    """
    Exercise 1: Temperature Conversion
    Convert a list of temperatures from Celsius to Fahrenheit.
    Formula: F = (C * 9/5) + 32
    """
    celsius_temps = [0, 10, 20, 30, 100]

    # Your solution here using map()
    fahrenheit_temps = map(convert_temperature, celsius_temps)

    print(f"Celsius: {celsius_temps}")
    print(f"Fahrenheit: {list(fahrenheit_temps)}")
    # Expected: [32.0, 50.0, 68.0, 86.0, 212.0]

def convert_temperature(degree):
    return (degree*1.8) + 32

exercise_1_map()
# %%
def exercise_2_map():
    """
    Exercise 2: String Manipulation
    Given a list of names, create a list of email addresses.
    Format: firstname.lastname@company.com (all lowercase)
    """
    names = ["John Doe", "Jane Smith", "Bob Wilson", "Alice Brown"]

    # Your solution here using map()
    emails = map(lambda x: f'{x.lower().replace(" ", ".")}@company.com', names)

    print(f"Names: {names}")
    print(f"Emails: {list(emails)}")
    # Expected: ['john.doe@company.com', 'jane.smith@company.com', ...]

exercise_2_map()
# %%
def exercise_3_map():
    """
    Exercise 3: Dictionary Transformation
    Extract specific fields from a list of user dictionaries.
    Return a list of tuples: (name, age)
    """
    users = [
        {"name": "Alice", "age": 30, "city": "NYC"},
        {"name": "Bob", "age": 25, "city": "LA"},
        {"name": "Charlie", "age": 35, "city": "Chicago"},
    ]

    # Your solution here using map()
    user_info = map(lambda x: (x['name'], x['age']), users)

    print(f"User info: {list(user_info)}")
    # Expected: [('Alice', 30), ('Bob', 25), ('Charlie', 35)]

exercise_3_map()
# =============================================================================
# FILTER EXERCISES
# =============================================================================

# %%
def exercise_4_filter():
    """
    Exercise 4: Even Numbers
    Filter out odd numbers from a list, keeping only even numbers.
    """
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    # Your solution here using filter()
    even_numbers = filter(lambda x: x%2==0, numbers)

    print(f"Original: {numbers}")
    print(f"Even numbers: {list(even_numbers)}")
    # Expected: [2, 4, 6, 8, 10, 12]

exercise_4_filter()
# %%
def exercise_5_filter():
    """
    Exercise 5: String Filtering
    Filter strings that start with a vowel (a, e, i, o, u).
    """
    words = ["apple", "banana", "orange", "grape", "kiwi", "elderberry", "mango"]

    # Your solution here using filter()
    vowel_words = filter(lambda word: word[0].lower() in 'aieou', words)

    print(f"All words: {words}")
    print(f"Words starting with vowel: {list(vowel_words)}")
    # Expected: ['apple', 'orange', 'elderberry']


exercise_5_filter()
# %%
def exercise_6_filter():
    """
    Exercise 6: Complex Filtering
    Filter users who are adults (age >= 18) and from "USA".
    """
    users = [
        {"name": "Alice", "age": 30, "country": "USA"},
        {"name": "Bob", "age": 17, "country": "USA"},
        {"name": "Charlie", "age": 25, "country": "UK"},
        {"name": "Diana", "age": 22, "country": "USA"},
        {"name": "Eve", "age": 16, "country": "Canada"},
    ]

    # Your solution here using filter()
    eligible_users = filter(lambda user: user['age']>=18 and user['country']=="USA", users)

    print(f"Eligible users: {list(eligible_users)}")
    # Expected: [{'name': 'Alice', ...}, {'name': 'Diana', ...}]

exercise_6_filter()
# =============================================================================
# ZIP EXERCISES
# =============================================================================

# %%
def exercise_7_zip():
    """
    Exercise 7: Combine Lists
    Combine three lists (names, ages, cities) into a list of tuples.
    """
    names = ["Alice", "Bob", "Charlie"]
    ages = [30, 25, 35]
    cities = ["NYC", "LA", "Chicago"]

    # Your solution here using zip()
    combined = zip(names, ages, cities)

    print(f"Combined data: {list(combined)}")
    # Expected: [('Alice', 30, 'NYC'), ('Bob', 25, 'LA'), ('Charlie', 35, 'Chicago')]

exercise_7_zip()
# %%
def exercise_8_zip():
    """
    Exercise 8: Create Dictionary
    Create a dictionary from two lists using zip().
    Keys: product names, Values: prices
    """
    products = ["laptop", "mouse", "keyboard", "monitor"]
    prices = [1200, 25, 75, 300]

    # Your solution here using zip() and dict()
    price_dict = dict(zip(products, prices))

    print(f"Price dictionary: {price_dict}")
    # Expected: {'laptop': 1200, 'mouse': 25, 'keyboard': 75, 'monitor': 300}

exercise_8_zip()
# %%
def exercise_9_zip():
    """
    Exercise 9: Parallel Iteration with zip()
    Calculate the dot product of two vectors using zip().
    Dot product: sum of (a[i] * b[i]) for all i
    """
    vector_a = [1, 2, 3, 4]
    vector_b = [5, 6, 7, 8]

    # Your solution here using zip() and sum()
    dot_product = sum(map(lambda x: x[0]*x[1],zip(vector_a, vector_b)))
    # dot_product = sum(a * b for a, b in zip(vector_a, vector_b))
    print(f"Vector A: {vector_a}")
    print(f"Vector B: {vector_b}")
    print(f"Dot product: {dot_product}")
    # Expected: 70 (1*5 + 2*6 + 3*7 + 4*8)


exercise_9_zip()
# =============================================================================
# REDUCE EXERCISES
# =============================================================================

# %%
def exercise_10_reduce():
    """
    Exercise 10: Sum of Numbers
    Calculate the sum of all numbers using reduce().
    """
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Your solution here using reduce()
    total = reduce(lambda accumulate,x: accumulate+x, numbers )

    print(f"Numbers: {numbers}")
    print(f"Sum: {total}")
    # Expected: 55

exercise_10_reduce()
# %%
def exercise_11_reduce():
    """
    Exercise 11: Find Maximum
    Find the maximum value in a list using reduce().
    """
    numbers = [45, 12, 89, 34, 67, 23, 91, 56]

    # Your solution here using reduce()
    maximum = reduce(lambda accumulate, x: accumulate if accumulate>x else x, numbers )

    print(f"Numbers: {numbers}")
    print(f"Maximum: {maximum}")
    # Expected: 91

exercise_11_reduce()
# %%
def exercise_12_reduce():
    """
    Exercise 12: Flatten Nested List
    Flatten a 2D list into a 1D list using reduce().
    """
    nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9], [10]]

    # Your solution here using reduce()
    flattened = reduce(lambda accumulate, x: accumulate + x, nested_list)

    print(f"Nested: {nested_list}")
    print(f"Flattened: {flattened}")
    # Expected: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
exercise_12_reduce()
# %%
def count_word(acc, word):
    acc[word] = acc.get(word, 0) + 1
    return acc

def exercise_13_reduce():
    """
    Exercise 13: Count Word Occurrences
    Count occurrences of each word using reduce() to build a dictionary.
    """
    words = ["apple", "banana", "apple", "cherry", "banana", "apple", "date"]

    # Your solution here using reduce()
    word_count = reduce(count_word, words, {})

    print(f"Words: {words}")
    print(f"Word count: {word_count}")
    # Expected: {'apple': 3, 'banana': 2, 'cherry': 1, 'date': 1}


exercise_13_reduce()
# =============================================================================
# COMBINED EXERCISES (Using multiple functions)
# =============================================================================

# %%
def exercise_14_combined():
    """
    Exercise 14: Data Pipeline
    Given a list of transactions, calculate the total value of successful
    transactions over $100.

    Use filter() to get successful transactions over $100,
    then map() to extract amounts,
    then reduce() to sum them.
    """
    transactions = [
        {"id": 1, "amount": 150, "status": "success"},
        {"id": 2, "amount": 80, "status": "success"},
        {"id": 3, "amount": 200, "status": "failed"},
        {"id": 4, "amount": 120, "status": "success"},
        {"id": 5, "amount": 95, "status": "success"},
        {"id": 6, "amount": 300, "status": "success"},
    ]

    # Your solution here using filter(), map(), and reduce()
    success = filter(
        lambda x: x["status"] == "success" and x["amount"] > 100, transactions
    )
    amount = map(lambda x: x['amount'], success)
    total = reduce(lambda acc,x: acc+x, amount, 0)

    print(f"Total successful transactions over $100: ${total}")
    # Expected: 570 (150 + 120 + 300)
exercise_14_combined()
# %%
def exercise_15_combined():
    """
    Exercise 15: Student Grade Analysis
    Given student data, find the average score of students who passed (score >= 60).

    Use filter() to get passing students,
    then map() to extract scores,
    then reduce() to calculate average.
    """
    students = [
        {"name": "Alice", "score": 85},
        {"name": "Bob", "score": 45},
        {"name": "Charlie", "score": 92},
        {"name": "Diana", "score": 78},
        {"name": "Eve", "score": 55},
        {"name": "Frank", "score": 88},
    ]

    # Your solution here
    passed = filter(lambda x: x['score']>=60, students)
    scores = list(map(lambda x: x['score'], passed))
    average_passing_score = reduce(lambda acc,x: acc+x,scores,0)/len(scores)

    print(f"Average passing score: {average_passing_score}")
    # Expected: 85.75 ((85 + 92 + 78 + 88) / 4)
exercise_15_combined()
# %%
def exercise_16_combined():
    """
    Exercise 16: Product Inventory Analysis
    Given two lists (products and stock), create a dictionary of in-stock products
    with their details.

    Use zip() to combine the lists,
    then filter() to keep only items with stock > 0,
    then map() to format the output.
    """
    products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Webcam"]
    stock = [5, 0, 12, 3, 0]
    prices = [999, 25, 79, 299, 89]

    # Your solution here
    in_stock = None

    print(f"In-stock products: {list(in_stock)}")
    # Expected format: [("Laptop", 5, 999), ("Keyboard", 12, 79), ("Monitor", 3, 299)]


# =============================================================================
# BONUS CHALLENGE
# =============================================================================

# %%

def calculate_order_total(order):
    return reduce(
        lambda acc, item: acc + (item['price'] * item['quantity']),
        order['items'],
        0
    )

def is_qualifying_order(order):
    if order['status'] != 'completed':
        return False
    return calculate_order_total(order) >= 50


def bonus_challenge():
    """
    BONUS: E-commerce Order Processing

    You have a list of orders. Each order contains items with quantities and prices.
    Calculate the total revenue from orders where:
    1. Order status is "completed"
    2. Total order value is >= $50

    Use a combination of map(), filter(), and reduce().
    """
    orders = [
        {
            "id": 1,
            "status": "completed",
            "items": [
                {"name": "Widget", "price": 10, "quantity": 3},
                {"name": "Gadget", "price": 25, "quantity": 2},
            ],
        },
        {
            "id": 2,
            "status": "completed",
            "items": [{"name": "Tool", "price": 15, "quantity": 1}],
        },
        {
            "id": 3,
            "status": "cancelled",
            "items": [{"name": "Device", "price": 100, "quantity": 1}],
        },
        {
            "id": 4,
            "status": "completed",
            "items": [
                {"name": "Component", "price": 30, "quantity": 2},
                {"name": "Part", "price": 20, "quantity": 1},
            ],
        },
    ]

    # Your solution here
    qualifying_orders = filter(is_qualifying_order, orders)
    order_totals = map(calculate_order_total, qualifying_orders)
    total_revenue = reduce(lambda acc, x: acc + x, order_totals, 0)


    print(f"Total revenue from qualifying orders: ${total_revenue}")
    # Expected: 160 (Order 1: 80, Order 4: 80. Order 2 is only 15, Order 3 cancelled)


# =============================================================================
# MAIN - Uncomment to test your solutions
# =============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("MAP EXERCISES")
    print("=" * 70)
    # exercise_1_map()
    # exercise_2_map()
    # exercise_3_map()

    print("\n" + "=" * 70)
    print("FILTER EXERCISES")
    print("=" * 70)
    # exercise_4_filter()
    # exercise_5_filter()
    # exercise_6_filter()

    print("\n" + "=" * 70)
    print("ZIP EXERCISES")
    print("=" * 70)
    # exercise_7_zip()
    # exercise_8_zip()
    # exercise_9_zip()

    print("\n" + "=" * 70)
    print("REDUCE EXERCISES")
    print("=" * 70)
    # exercise_10_reduce()
    # exercise_11_reduce()
    # exercise_12_reduce()
    # exercise_13_reduce()

    print("\n" + "=" * 70)
    print("COMBINED EXERCISES")
    print("=" * 70)
    # exercise_14_combined()
    # exercise_15_combined()
    # exercise_16_combined()

    print("\n" + "=" * 70)
    print("BONUS CHALLENGE")
    print("=" * 70)
    # bonus_challenge()
