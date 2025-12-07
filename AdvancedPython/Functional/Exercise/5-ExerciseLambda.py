#%%

my_list = [5, 4, 3]

print(list(map(lambda x: x**2, my_list)))

#%%
# List Sorting, sort by second element
a = [(0,2),(4,3),(10,-1),(9,9)]
a.sort(key=lambda x: x[1])
print(a)
# %%
