import pdb
# Exercise 5: The Lost Items
# This function should return items that appear in both lists
# Something is causing it to miss matches. Debug it!


def find_common_items(list1, list2):
    common = []
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                common.append(list1[i])
                
    breakpoint()
    return list(set(common))


# Test - uncomment to run:
# result = find_common_items(["apple", "banana", "cherry"], ["banana", "date", "cherry", "fig"])
# print(f"Result: {result}")
# Expected output: ['banana', 'cherry'] (order may vary)