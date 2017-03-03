#Write a Python program to count the number of characters (character frequency) in a string.
def char_frequency(str1):
...     dict={}
...     for s in str1:
...             keys=dict.keys()
...             if s in keys:
...                     dict[s]+=1
...             else:
...                     dict[s]=1
...     return dict
...
>>> print(char_frequency('hit.ac.zw'))
{'a': 1, 'c': 1, 'i': 1, 'h': 1, '.': 2, 't': 1, 'w': 1, 'z': 1}
>>> print(char_frequency('simba.com'))
{'a': 1, 'c': 1, 'b': 1, 'i': 1, 'm': 2, 'o': 1, '.': 1, 's': 1}
