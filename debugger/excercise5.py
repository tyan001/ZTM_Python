#Exercise 4: The Mixed-Up Dictionary
# This function should count occurrences of each character in a string
# But the counts are off by one... Why?


def count_characters(text):
    counts = {}
    for char in text:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    breakpoint()
    return counts


# Test - uncomment to run:
result = count_characters("banana")
print(f"Result: {result}")
# Expected output: {'b': 1, 'a': 3, 'n': 2}
