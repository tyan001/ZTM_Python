# %%
import re
# %%
string = "Search this inside of this text please!"

print('Search' in string)
# %%

a = re.search('this', string)
a
# %%
a.group()
# %%
pattern = re.compile('this')

a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)

print(a)
print(b)
print(c)

pattern2 = re.compile("Search this inside of this text please!")
d = pattern2.fullmatch(string)
print(d)
# %%
