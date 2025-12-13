# %% Exercise 1: Validate Phone Numbers - SOLUTION
"""
Write a function that checks if a string is a valid US phone number.
Valid formats:
- 123-456-7890
- (123) 456-7890
- 123 456 7890
- 123.456.7890

Return True if valid, False otherwise.
"""

import re


def is_valid_phone(phone: str) -> bool:
    pattern = r"^(\(\d{3}\)|\d{3})[-.\s]\d{3}[-.\s]\d{4}$"
    return bool(re.match(pattern, phone))


# Breakdown:
# ^                 Start of string
# (\(\d{3}\)|\d{3}) Either (123) OR 123 - parentheses need escaping \( \)
# [-.\s]            Separator: dash, dot, or space
# \d{3}             3 digits
# [-.\s]            Separator again
# \d{4}             4 digits
# $                 End of string


# Tests (uncomment to run)
# print(is_valid_phone("123-456-7890"))
# Expected: True

# print(is_valid_phone("(123) 456-7890"))
# Expected: True

# print(is_valid_phone("123 456 7890"))
# Expected: True

# print(is_valid_phone("123.456.7890"))
# Expected: True

# print(is_valid_phone("1234567890"))
# Expected: False

# print(is_valid_phone("12-34-5678"))
# Expected: False


# %% Exercise 1B: Validate Social Security Numbers (Similar Practice)
"""
Write a function that checks if a string is a valid US Social Security Number (SSN).
Valid formats:
- 123-45-6789
- 123 45 6789
- 123.45.6789

Invalid:
- 123456789 (no separators)
- 123-456-789 (wrong grouping)
- 12-345-6789 (wrong grouping)

Return True if valid, False otherwise.

Hint: SSN format is 3 digits, separator, 2 digits, separator, 4 digits
"""
import re


def is_valid_ssn(ssn: str) -> bool:
    pattern = r"^(\d{3})[-.\s](\d{2})[-.\s](\d{4})$"
    return bool(re.match(pattern,ssn))


# Tests (uncomment to run)
print(is_valid_ssn("123-45-6789"))
# Expected: True

print(is_valid_ssn("123 45 6789"))
# Expected: True

print(is_valid_ssn("123.45.6789"))
# Expected: True

print(is_valid_ssn("123456789"))
# Expected: False

print(is_valid_ssn("123-456-789"))
# Expected: False

print(is_valid_ssn("12-345-6789"))
# Expected: False


# %% Exercise 2: Extract Email Addresses
"""
Write a function that extracts all email addresses from a given text.
Return a list of email addresses found.

Hint: Email format is generally: something@something.something
"""
import re


def extract_emails(text: str) -> list:
    pattern = r"[\w.-]+@[\w.-]+\.\w+"
    return re.findall(pattern, text)

# Breakdown:
# [\w.-]+    One or more word chars, dots, or hyphens (username)
# @          Literal @ symbol
# [\w.-]+    One or more word chars, dots, or hyphens (domain)
# \.         Literal dot (escaped because . means "any char")
# \w+        One or more word chars (extension like com, org, uk)

# Tests (uncomment to run)
test_text = """
Contact us at support@example.com or sales@company.org
Personal emails: john.doe@gmail.com, jane_doe123@yahoo.co.uk
Invalid: @nodomain.com, missing@, plain text
"""
print(extract_emails(test_text))
# Expected: ['support@example.com', 'sales@company.org', 'john.doe@gmail.com', 'jane_doe123@yahoo.co.uk']


# %% Exercise 3: Password Strength Validator
"""
Write a function that checks if a password meets these criteria:
- At least 8 characters long
- Contains at least one uppercase letter
- Contains at least one lowercase letter
- Contains at least one digit
- Contains at least one special character (!@#$%^&*()_+-=)

Return True if all criteria met, False otherwise.

Hint: You might want to use multiple regex patterns or lookaheads (?=...)
"""
import re


# Approach 1: Multiple separate checks (easier to read and debug)
def is_strong_password(password: str) -> bool:
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"\d", password):
        return False
    if not re.search(r"[!@#$%^&*()_+-=]", password):
        return False
    return True


# Approach 2: Lookaheads (all in one pattern)
def is_strong_password_v2(password: str) -> bool:
    pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*()_+-=]).{8,}$"
    return bool(re.match(pattern, password))


# Breakdown of lookahead pattern:
# ^                     Start of string
# (?=.*[A-Z])           Lookahead: must contain at least one uppercase
# (?=.*[a-z])           Lookahead: must contain at least one lowercase
# (?=.*\d)              Lookahead: must contain at least one digit
# (?=.*[!@#$%^&*()_+-=])  Lookahead: must contain at least one special char
# .{8,}                 Match at least 8 of any character
# $                     End of string


# Tests (uncomment to run)
# print(is_strong_password("Abc123!@"))
# Expected: True

# print(is_strong_password("SecureP@ss1"))
# Expected: True

# print(is_strong_password("weakpass"))
# Expected: False (no uppercase, digit, or special char)

# print(is_strong_password("ALLCAPS123!"))
# Expected: False (no lowercase)

# print(is_strong_password("Short1!"))
# Expected: False (less than 8 characters)


# %% Exercise 4: Find and Replace Dates
"""
Write a function that finds dates in MM/DD/YYYY format and converts them
to YYYY-MM-DD format (ISO format).

Example: "Meeting on 12/25/2024" -> "Meeting on 2024-12-25"
"""
import re


def convert_dates(text: str) -> str:
    # Your code here
    pass


# Tests (uncomment to run)
# print(convert_dates("Meeting on 12/25/2024"))
# Expected: "Meeting on 2024-12-25"

# print(convert_dates("Events: 01/15/2025, 06/30/2025, and 12/01/2025"))
# Expected: "Events: 2025-01-15, 2025-06-30, and 2025-12-01"

# print(convert_dates("No dates here"))
# Expected: "No dates here"


# %% Exercise 5: Extract Hashtags and Mentions
"""
Write a function that extracts all hashtags and mentions from social media text.
- Hashtags start with # followed by word characters
- Mentions start with @ followed by word characters

Return a dictionary with two keys: 'hashtags' and 'mentions', each containing a list.
"""
import re


def extract_tags(text: str) -> dict:
    # Your code here
    pass


# Tests (uncomment to run)
# test_post = "Just met @john_doe at #PyCon2024! Great talk about #Python and #MachineLearning. Thanks @jane_smith for the intro!"
# print(extract_tags(test_post))
# Expected: {'hashtags': ['#PyCon2024', '#Python', '#MachineLearning'], 'mentions': ['@john_doe', '@jane_smith']}

# print(extract_tags("No tags here, just plain text."))
# Expected: {'hashtags': [], 'mentions': []}

# print(extract_tags("#solo hashtag"))
# Expected: {'hashtags': ['#solo'], 'mentions': []}
