#ifelse condition

#//Syntax
#if <condition>:
    #statement
#else:
    #statment

#example1
if 10<8:
    print('hey it right')
    print('if condition')
else:
    print('hey it wrong')
    print('else condition')

#example2
print(10>8) #//True
print(10<8) #//False


#example3
x=int(input('Enter a number to check numvber is even or odd:'))
if x%2==0:
    print('even')
else:
    print('odd')


#example4
users=['kakshil','dwait','khushali']
users=input('Enter user name:')
if 'kakshil' in users:
    print('kakshil Is Present')
elif 'dwait' in users:
    print('dwait Is Present')
elif 'khushali' in users:
    print('khushali Is Present')
else:
    print('User Not Exist')

#example5
list=[]
list=input('enter any number or character:')
if list:
    print('list is not empty')
else:
    print('List Empty')
