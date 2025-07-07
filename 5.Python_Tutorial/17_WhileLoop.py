#While loop it check condition is true till that it will run code and if condition is false then it break condition and
#stop..
from pickle import FALSE

#example




'''
active=True
while active:
    user=input('enter a number or Press Q for Quite: ')
    if user == 'exit':
        active=False
        print('exiting....')
        break
    if user != 'exit':
     if user.isdigit():
        if int(user) % 2 == 0:
            print(f'{user}  even')
        if int(user) % 2 != 0:
            print(f'{user}  odd')
'''


num=[1,2,3,4,2,5,2]
while 2 in num:
    num.remove(2)
    print(num)
    #/while used because it remove all duplicate from list








