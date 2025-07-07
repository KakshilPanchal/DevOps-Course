#//Function
#/syntax
# def <functionName>():
    #Statement
#calling function
# <function name>()


#//example
'''

def myfun(name,age,*hobbies):  #//if we dont provide age during calling function
    # then you can define age in during defining function
    #*Hobbies considered as list were you write diff thing as list..
    print('*' * 20)
    print(f'Welcome User {name} ')
    print('Hobbies are: ')
    for hobby in hobbies:
     print(f' ->  {hobby}')
    print(f'age is {age}')
    print('thank you for signing in.....')
    print('*' * 20)

myfun('kakshil',18,'singing', 'cricket', 'gaming')   #//calling function to execute code inside Function
myfun('khushali',23,'cricket', 'football','singing')
myfun('dwait',21,'singing','Dancing','Music')

'''

#----------------------------------------------------------------------------------------------------------------------

#Example - 2  DYNAMIC CHANGNG VALUE FOR EACH TIME.. Function Arguments..................
'''
def myfun(name, surname , **userinfo):  #//if we dont provide age during calling function
    # then you can define age in during defining function
    #**Hobbies(double star)--> dictionaries value means key:value. (   DYNAMIC VALUE )
    print('*' * 20)
    print(f'Welcome User {name} {surname} ')

    for key, value in userinfo.items():
        print(f' -> {key} is {value}')
    print('thank you for signing in.....')
    print('*' * 20)

myfun('kakshil','panchal',age=18,city='ahmedabad',email='kakshil@gmail.com',hobbies='golf ,cricket ,gaming.')   #//calling function to execute code inside Function
myfun('khushali','nagar',age=23,city='Surat',email='khushali@gmail.com',hobbies='football ,singing.')
myfun('dwait','vaidya')
'''
#---------------------------------------------------------------------------------------------------------------------

#//Return Keyword in Functions...........
#return means  the value throw into output
def add(num1,num2):
    return num1 + num2
result=add(1, 2)
print(result)












