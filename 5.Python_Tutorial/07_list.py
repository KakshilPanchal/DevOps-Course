#List --> to store more than one value in Variable
from pyexpat import native_encoding

#syntax
#['value1', 'value2'...]
name=['kakshil', 'raju','dwait','khushali']
# to get sepcific value from list
print(name[0])
print(name[0:2])

#To add value in list
name.append('sneha')
print(name) #it will add value in last

#to remove value from list
#name.remove ('raju')
#print(name)

# to modify value in list
#name[2]='Sneha'
#print(name)

#to Insert value at specific position
#name.insert(1,"dwait_vaidya")
#print(name)

#to delete value using index No.
#del name[2]
#print(name)

#find length of values in list
#print(len(name))


#---------------------------------------------------------------------------------------------------
#Sorting of List
name.sort()
print(name)

name.sort(reverse=True)
print(name)

name.reverse()
print(name)
#--------------------------------------------------------------------------------------------

#Popping Item in list
#it will remove the last value from list

#print(name.pop())
#pop will show the deleted value

#print(name)

#print(name.remove('dwait_vaidya'))
#it will not show the deleted value

#print(name)
#print(name.pop(0)) # to remove specific index no values
#print(name)

#to get middle value using index No
print(name[1:3])

#to get last two value using index no
print(name[-2:])
#--------------------------------------------------------------------------------------------

#Numeric List

marks=[10,20.90,30.2,40]
print(marks)
print(min(marks))  #Minimum
print(max(marks))  #Maximum
print(sum(marks))  #total num
print(len(marks))  #lenght of marks

mix_list=['kakshil', 18, "ahmedabad"]
print(mix_list)