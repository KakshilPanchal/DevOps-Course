#random will use to print any number or string automatically. it is Modules for generating random numbers
import random
from math import radians
'''
print(random.random()) #?/floating value return

print(random.randint(1, 10)) #//return integer value

print(random.uniform(1, 10)) #

content=['kakshil','dwait','khushali','sneha',1,2]
print(random.choice(content))  #//choice it will pick random content from list,tuple,string.
print(content)

random.shuffle(content)  #// sequence of content will be changed.
print(content)

random.seed(1,10)
print(random.random())
'''
#-------------------------------------------------------------------------------------

#example
while True:
    a= random.randint(1,10)
    print(f'number is {a}')
    user=input('do you want to continue?(y/n): ')
    if user == 'y':
        continue
    else:
        break