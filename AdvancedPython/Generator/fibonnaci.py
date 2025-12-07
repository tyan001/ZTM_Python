#%%
from time import time
def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f"took {t2 - t1} s")
        return result
    
    return wrapper

#%%

def fib(x):
    
    if x == 0:
        return 0
    elif x in [1,2]:
        return 1
    
    return fib(x - 1) + fib(x - 2)

# %%
lst_fib = [fib(x) for x in range(21)]
print(lst_fib)
# %%

def gen_fib(x):
    
    a = 0
    b = 1
    
    for i in range(x):
        yield a
        temp = a 
        a = b
        b = temp + b
      
for x in gen_fib(21):
    print(x)
# %%
def lst_fib(x):
    a = 0
    b = 1
    result = []
    for i in range(x):
        result.append(a)
        temp = a
        a = b
        b = temp + b
    
    return result


for x in lst_fib(21):
    print(x)
