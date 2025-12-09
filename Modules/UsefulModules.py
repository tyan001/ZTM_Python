#%%
from collections import Counter, defaultdict
import datetime

#%%
li = [1,2,3,4,5,6,7,7,7,7,7,7]
print(Counter(li))
print(Counter(a=4,d=5))
temp = Counter(li)
for k,v in temp.items():
    print(f'Key {k}, Value {v}')
        
#%%        
dictionary = {'a': 1, "b": 2}
print(dictionary['a'])

tmp_dict = {"a": 1, "b": 2}
dictionary = defaultdict(lambda: 'Does not exist', tmp_dict)
print(dictionary['a'])
print(dictionary['c'])
print(dictionary.items())
#%%
print(datetime.date.today())

# %%
