import pdb
# Exercise 3: The Broken Calculator
# This function should calculate: (a + b) * c / d
# Users report getting wrong answers. Find the bug!


def calculate(a, b, c, d):
    step1 = a + b
    step2 = step1 * c
    # step3 = step2 / b
    step3 = step2 / d
    breakpoint()
    return step3


# Test - uncomment to run:
# result = calculate(10, 5, 2, 5)
# print(f"Result: {result}")
# Expected output: 6.0 (because (10 + 5) * 2 / 5 = 30 / 5 = 6.0)