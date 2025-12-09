import pdb
# Exercise 2: The Faulty Filter
# This function should return only words longer than min_length
# But it's returning wrong results... Debug to find why!


def filter_long_words(words, min_length):
    long_words = []
    for word in words:
        if len(word) > min_length:
            long_words.append(word)
        # long_words = []
        breakpoint()
    return long_words


# Test - uncomment to run:
result = filter_long_words(["cat", "elephant", "dog", "hippopotamus", "ant"], 3)
# print(f"Result: {result}")
# Expected output: ['elephant', 'hippopotamus']
