"""
Here we test whether relatively basic stuff works cuz I forgot
"""

dic: dict = {1: 2, 3: 4, 5: 6}
print(dic.keys())
empty_list: list = []
for key in dic.keys():
    print(key)
    empty_list.append(key)

print(empty_list)

