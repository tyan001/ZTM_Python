# %% Exercise 1: Basic Division Safety
# Write a function `safe_divide(a, b)` that:
# - Returns the result of a / b
# - If division by zero occurs, return None
# - Print "Division successful" only when no error occurs


def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Division by zero encountered")
        return None
    else:
        print("Division successful")
        return result


safe_divide(10, 2)
# Expected: prints "Division successful", returns 5.0

safe_divide(10, 0)
# Expected: returns None (no success message)


# %% Exercise 2: File Reader with Cleanup
# Write a function `read_first_line(filename)` that:
# - Tries to open and read the first line of a file
# - Returns the first line if successful
# - Returns "File not found" if FileNotFoundError occurs
# - Always prints "Attempted file operation" regardless of outcome


def read_first_line(filename):
    try:
        with open(filename, "r") as file:
            line = file.readline().strip()
            return line
    except FileNotFoundError:
        return "File not found"
    finally:
        print("Attempted file operation")


read_first_line("nonexistent.txt")
# Expected: prints "Attempted file operation", returns "File not found"
# Can create the file and read the first line to test

# %% Exercise 3: Integer Converter
# Write a function `convert_to_int(value)` that:
# - Tries to convert the value to an integer
# - Returns the integer if successful
# - Returns "Invalid input" for ValueError
# - Returns "Unexpected error" for any other exception
# - Prints "Conversion complete" in all cases


def convert_to_int(value):
    try:
        val = int(value)
        return val
    except ValueError:
        return "Invalid input"
    except Exception:
        return "Unexpected error"
    finally:
        print("Conversion Complete")


print(convert_to_int("42"))
# Expected: prints "Conversion complete", returns 42

print(convert_to_int("hello"))
# Expected: prints "Conversion complete", returns "Invalid input"

print(convert_to_int(None))
# Expected: prints "Conversion complete", returns "Unexpected error"


# %% Exercise 4: List Index Accessor
# Write a function `safe_get(lst, index)` that:
# - Returns the element at the given index
# - Returns "Index out of range" for IndexError
# - Returns "Invalid index type" for TypeError
# - Prints "Access attempted" in the finally block
# - Prints "Element retrieved successfully" only on success


def safe_get(lst, index):
    try:
        element = lst[index]
    except IndexError:
        return "Index out of range"
    except TypeError:
        return "Invalid index type"
    else:
        print("Element retrieved successfully")
        return element
    finally:
        print("Access attempted")


safe_get([1, 2, 3], 1)
# Expected: prints "Element retrieved successfully", "Access attempted", returns 2

safe_get([1, 2, 3], 10)
# Expected: prints "Access attempted", returns "Index out of range"

safe_get([1, 2, 3], "one")
# Expected: prints "Access attempted", returns "Invalid index type"


# %% Exercise 5: Dictionary Key Fetcher with Logging
# Write a function `fetch_key(data, key)` that:
# - Returns the value for the given key
# - Catches KeyError and returns f"Key '{key}' not found"
# - In the else block, print f"Successfully retrieved: {value}"
# - In the finally block, append the key to a global list called `access_log`

access_log = []


def fetch_key(data, key):
    try: 
        val = data[key]
    except KeyError:
        return f"Key '{key}' no found"
    else:
        print(f"Successfully retrieved: {val}")
    finally:
        access_log.append(key)
    pass  # Your code here


fetch_key({"name": "Alice", "age": 30}, "name")
# Expected: prints "Successfully retrieved: Alice", returns "Alice"
# access_log should contain "name"

fetch_key({"name": "Alice"}, "email")
# Expected: returns "Key 'email' not found"
# access_log should contain "name", "email"


# %% Exercise 6: Nested Error Handling
# Write a function `process_user_data(data)` that:
# - data is expected to be a dict with "age" key containing a string number
# - Convert data["age"] to int and return it doubled
# - Handle KeyError: return "Missing age field"
# - Handle ValueError: return "Age must be a valid number"
# - On success, print "Processing successful"
# - Always print "Processing attempt finished"


def process_user_data(data):
    try:   
        val = int(data['age']) * 2
    except KeyError:
        return "Missing age field"
    except ValueError:
        return "Age must be a valid number"
    else: 
        print(f"Processing successful age {val}")
        return val
    finally:
        print("Processing attempt finished")
    


# process_user_data({"age": "25"})
# Expected: prints "Processing successful", "Processing attempt finished", returns 50

# process_user_data({"name": "Bob"})
# Expected: prints "Processing attempt finished", returns "Missing age field"

# process_user_data({"age": "twenty"})
# Expected: prints "Processing attempt finished", returns "Age must be a valid number"


# %% Exercise 7: Resource Manager Simulation
# Write a function `use_resource(should_fail)` that:
# - Prints "Acquiring resource"
# - If should_fail is True, raise a RuntimeError("Resource failed")
# - If should_fail is False, print "Resource used successfully" in else block
# - Always print "Releasing resource" in finally block
# - Return "Success" or let the error propagate


def use_resource(should_fail):
    try:
        print("Acquiring resource")
        if should_fail:
            raise RuntimeError("Resource failed")
    except RuntimeError:
        raise
    else:
        print("Resource used successfully")
        return "Success"
    finally:
        print("Releasing resource")



# use_resource(False)
# Expected output:
#   Acquiring resource
#   Resource used successfully
#   Releasing resource
# Returns: "Success"

use_resource(True)
# Expected output:
#   Acquiring resource
#   Releasing resource
# Then raises: RuntimeError: Resource failed





# %%
