# %%
some_list = ["a", "b", "c", "b", "d", "m", "n", "n"]

duplicates = list(set(char for char in some_list if some_list.count(char) > 1))
print(duplicates)

# %%
# Problem 1: List Comprehension - Square Even Numbers
# Create a list of squares for even numbers from 1 to 20
# Expected: [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]
lst = list(range(1, 21))
result = [x**2 for x in lst if x % 2 == 0]
print(result)
# %%
# Problem 2: List Comprehension - Filter Strings
words = ["python", "java", "c++", "javascript", "ruby", "go", "rust"]
# Create a list of words that contain the letter 'a' and have more than 3 characters
# Expected: ['java', 'javascript']

result = [word for word in words if "a" in word and len(word) > 3]
print(result)

# %%
# Problem 3: Set Comprehension - Unique Lengths
sentences = ["hello world", "python is fun", "coding", "set comprehension", "ai"]
# Create a set of unique word lengths from all words in all sentences
# Expected: {2, 3, 5, 6, 13} (order may vary)
result = set(len(word) for sentence in sentences for word in sentence.split(" "))
print(result)

# %%
# Problem 4: Dictionary Comprehension - Character Count
text = "comprehension"
# Create a dictionary with each character as key and its count as value
# Expected: {'c': 2, 'o': 2, 'm': 1, 'p': 1, 'r': 1, 'e': 2, 'h': 1, 'n': 2, 's': 1, 'i': 1}
result = {char: text.count(char) for char in text}
# result = {char: text.count(char) for char in set(text)}

print(result)
# %%
# Problem 5: List Comprehension - Nested Lists (Flattening)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Flatten the matrix into a single list
# Expected: [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = [value for array in matrix for value in array]
print(result)
# %%
# Problem 6: Dictionary Comprehension - Swap Keys and Values
original = {"a": 1, "b": 2, "c": 3, "d": 4}
# Create a new dictionary with swapped keys and values
# Expected: {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
result = {value: key for key, value in original.items()}
print(result)

# %%
# Problem 7: Set Comprehension - Common Divisors
numbers = [12, 18, 24, 30]
# Create a set of all numbers from 1 to 10 that divide evenly into ALL numbers in the list
# Expected: {1, 2, 3, 6}
result = set(
    divisor
    for divisor in list(range(1, 11))
    if all(num % divisor == 0 for num in numbers)
)

print(result)
# %%
# Problem 8: List Comprehension - Conditional Expression
temps_celsius = [-5, 0, 10, 20, 30, 40]
# Create a list of temperature descriptions: "freezing" if < 0, "cold" if 0-15, "warm" if 16-30, "hot" if > 30
# Expected: ['freezing', 'cold', 'cold', 'warm', 'warm', 'hot']
result = [
    "freezing"
    if temp < 0
    else "cold"
    if 0 <= temp <= 15
    else "warm"
    if 16 <= temp <= 30
    else "hot"
    for temp in temps_celsius
]

print(result)

# %%
# Problem 9: Dictionary Comprehension - Grade Classification
students = {"Alice": 85, "Bob": 72, "Charlie": 90, "David": 65, "Eve": 78}
# Create a dictionary with student names as keys and their grade letters as values
# A: 90+, B: 80-89, C: 70-79, D: 60-69, F: <60
# Expected: {'Alice': 'B', 'Bob': 'C', 'Charlie': 'A', 'David': 'D', 'Eve': 'C'}

result = {
    name: (
        "A"
        if value >= 90
        else "B"
        if value >= 80
        else "C"
        if value >= 70
        else "D"
        if value >= 60
        else "F"
    )
    for name, value in students.items()
}

print(result)
# %%
