"""
import pytest
import string

# 1. Write a function that takes the length of a side of a square as an argument and returns the area of the square.

def sq_area(side):
    area = side ** 2
    return area
sq_area(6)
# 36

2. Write a function that takes the heigth and width of a triangle and returns the area.

def tri_area(height, width):
    area = 0.5 * height * width
    return area
tri_area(4,6)
# 12.0

3. Write a function that takes a string as an argument and returns a tuple with the string converted to a list and the count of characters.

def tuple(string):
#    list = []
#    for i in string:
#        list = list + [i]
    x = len(string)
    list1 = list(string)
    tup = (list1, x)
    return tup
tuple('word')

# (['w', 'o', 'r', 'd'], 4)

4. Write a function that takes two integers passed as strings and returns the sum, difference, and product as a tuple (all values as integers).

def fun(str1, str2):
    int1 = int(str1)
    int2 = int(str2)
    tup = ()
    tup = tup + (int1 + int2, ) + (int1 - int2, ) + (int1 * int2, )
    return tup
fun('3', '5')

# (8, -2, 15)

5. Write a function that takes a list and returns a tuple where the first item is the list in reverse order and the second item is just the items with an odd index.

def tuple(var):
    reverse_list = var[::-1]
    odd_list = var[0::2]
    tup = reverse_list, odd_list
    return tup
tuple(['a', 'b', 'c', 'd'])

# (['d', 'c', 'b', 'a'], ['a', 'c'])

Challenge Problem: Write a function that returns the score for a word. Each letter's score is equal to it's position in the alphabet. The score of the word is the score of the letters.
So, for example:
A = 1, B = 2, C = 3, D = 4, E = 5
abe = 8 = (1 + 2 + 5)
Hint: The string library has a property ascii_lowercase that can save some typing here.

import string
value = {}
n = 1
for i in (string.ascii_lowercase):
    value[i] = n
    n += 1

def score(word):
    lower_word = word.lower()
    number = 0
    for i in lower_word:
        number = number + value[i]
    return number
score('abegT')

# 35
