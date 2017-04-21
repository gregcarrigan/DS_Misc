# -*- coding: utf-8 -*-
"""
Code to iterate through a list and test whether ech item is numeric
by trying to convert it to type float. If there is no error, the 
item is appended to a new file. If there is an error, the value is ignored.
"""

clean = []
corrupted = ['!1', '23.1', '23.4.5', '??12', '.12', '12-12', '-11.1', '0-1', '*12.1', '1000', ]
for i in corrupted:
    try:
        clean.append(float(i))
    except ValueError:
        continue
print (clean)