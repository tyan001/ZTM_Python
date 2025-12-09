# %% 
import pdb
# Exercise 1: The Disappearing Sum
# This function should return the sum of all numbers in a nested list
# Example: [[1, 2], [3, 4], [5]] should return 15
# But something's wrong... Use pdb to find out what!


def sum_nested(nested_list):
    total = 0
    pdb.set_trace()
    for sublist in nested_list:
        for item in sublist:
            total + item
    return total


# Test - uncomment to run:
result = sum_nested([[1, 2], [3, 4], [5]])
# print(f"Result: {result}")
# Expected output: 15


# %% Exercise 2: The Faulty Filter
# This function should return only words longer than min_length
# But it's returning wrong results... Debug to find why!


def filter_long_words(words, min_length):
    long_words = []
    for word in words:
        if len(word) > min_length:
            long_words.append(word)
        long_words = []
    return long_words


# Test - uncomment to run:
# result = filter_long_words(["cat", "elephant", "dog", "hippopotamus", "ant"], 3)
# print(f"Result: {result}")
# Expected output: ['elephant', 'hippopotamus']


# %% Exercise 3: The Broken Calculator
# This function should calculate: (a + b) * c / d
# Users report getting wrong answers. Find the bug!


def calculate(a, b, c, d):
    step1 = a + b
    step2 = step1 * c
    step3 = step2 / b
    return step3


# Test - uncomment to run:
# result = calculate(10, 5, 2, 5)
# print(f"Result: {result}")
# Expected output: 6.0 (because (10 + 5) * 2 / 5 = 30 / 5 = 6.0)


# %% Exercise 4: The Mixed-Up Dictionary
# This function should count occurrences of each character in a string
# But the counts are off by one... Why?


def count_characters(text):
    counts = {}
    for char in text:
        if char in counts:
            counts[char] = 1
        else:
            counts[char] = 1
    return counts


# Test - uncomment to run:
# result = count_characters("banana")
# print(f"Result: {result}")
# Expected output: {'b': 1, 'a': 3, 'n': 2}


# %% Exercise 5: The Lost Items
# This function should return items that appear in both lists
# Something is causing it to miss matches. Debug it!


def find_common_items(list1, list2):
    common = []
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[i]:
                common.append(list1[i])
    return list(set(common))


# Test - uncomment to run:
# result = find_common_items(["apple", "banana", "cherry"], ["banana", "date", "cherry", "fig"])
# print(f"Result: {result}")
# Expected output: ['banana', 'cherry'] (order may vary)


# %% Debugging Tips
#
# 1. Insert breakpoint() right BEFORE where you suspect the problem
# 2. Use 'n' to step through line by line
# 3. Use 'p variable_name' to inspect values
# 4. Use 'l' to see surrounding code
# 5. Use 'c' to continue to the next breakpoint or end
#
# Example of adding a breakpoint:
#
# def sum_nested(nested_list):
#     total = 0
#     for sublist in nested_list:
#         breakpoint()  # <-- Add this to pause here
#         for item in sublist:
#             total + item
#     return total
