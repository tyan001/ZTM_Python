#%%
from time import time
#%%

def generator_function(num):
    for i in range(num):
        yield i
    

# %%
for item in generator_function(5):
    print(item)
# %%

gen = generator_function(10)

# %%
print(next(gen))
# %%


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f"took {t2 - t1} s")
        return result

    return wrapper
# %%
@performance
def long_time():
    for i in range(100000000):
        i * 5
    return "done"

@performance
def long_time2():
    for i in list(range(100000000)):
        i * 5
    return "done"

# long_time()  # took 4.694
# long_time2()  # 9.528
# %%

def special_for(iterable):
    iterator = iter(iterable)
    
    while True:
        try:
            #print(iterator)
            print(next(iterator))
        except StopIteration:
            break


special_for([1, 2, 3])
# %%
class MyGen:
    current = 0
    def __init__(self, first, last):
        self.first = first
        self.last = last


    def __iter__(self):
        return self

    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration

mygen = MyGen(1, 100)
for i in mygen:
    print(i)
# %%
