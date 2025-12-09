# Exercise 1: The Disappearing Sum
# This function should return the sum of all numbers in a nested list
# Example: [[1, 2], [3, 4], [5]] should return 15
# But something's wrong... Use pdb to find out what!

def sum_nested(nested_list):
    total = 0

    for sublist in nested_list:
        for item in sublist:
            total = total + item  # Used to be just total + item
    breakpoint()
    return total


# Test - uncomment to run:
result = sum_nested([[1, 2], [3, 4], [5]])
print(f"Result: {result}")
# Expected output: 15

# %% Debugging Tips
#
# 1. Insert breakpoint() right BEFORE where you suspect the problem
# 2. Use 'n' to step through line by line
# 3. Use 'p variable_name' to inspect values
# 4. Use 'l' to see surrounding code
# 5. Use 'c' to continue to the next breakpoint or end
#

# locals()Shows all local variables in current scope
# globals()Shows all global variables (can be noisy)
# p locals()Print local variables
# pp locals() Pretty-print local variables (easier to read)

# Example of adding a breakpoint:
#
# def sum_nested(nested_list):
#     total = 0
#     for sublist in nested_list:
#         breakpoint()  # <-- Add this to pause here
#         for item in sublist:
#             total + item
#     return total
