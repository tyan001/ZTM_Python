#%%

def hello():
    print("Hellooooooooooooooooo")
    
# greet = hello()
greet = hello

# print(greet)
print(greet())
# %%
def hello(func):
    func()
    
def greet():
    print('still here!')
    
a = hello(greet)

print(a)

# %%
