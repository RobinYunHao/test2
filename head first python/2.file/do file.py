import os
from list import forlist
file = open('juben.txt')
for juben in file:
    try:
        (person,said) = juben.split(":",1)
        print person,"said:",said
    except(ValueError):
        pass

file.close()
