#//For loop --> Executed code of each item in sequence repatly

#//syntax
'''
for i in <condition>:
   statement
'''

#//example
for i in 1,2,3,4,5:  #store this number in i variable
    print('kakshil')
    print(i)

#/Example
num=['kakshil','dwait','khushali','kholi']
for user in num:
    print(user)

#//Example
age_info={'kakshil Panchal':20,'dwait vaidya':21,'khushali nagar':22}
for name,age in age_info.items(): #// for dictonaries used .items and if you want tp print key then used .key() and want
    #value then .value()
        print(f'name is : {name}')
        print(f'age is  : {age}')

#//example
for number in range(1,11):
    print(number) #//it will minus one in loop


