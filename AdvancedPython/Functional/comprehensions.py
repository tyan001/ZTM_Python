
#%%
lst1 = [char for char in 'hello']
lst1
#%%
lst2 = [num for num in range(0,50)]
lst2
#%%
lst3 = [num*2 for num in range(0, 50)]
lst3

#%%
lst4 = [num * 2 for num in range(0, 50) if  num%2==0]
lst4

#%%
simple_dict = {
    'a':1,
    'b':2
}
dict1 = {key*2:value**2 for key,value in simple_dict.items()}
dict1

#%%
dict2 = {num:num*2 for num in [1,2,3]}
dict2
# %%
