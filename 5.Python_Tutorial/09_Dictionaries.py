#Dictionaries
#based on key pair we stored the values in it
from sys import hash_info

#syntax
#we used curly bracket for dictionaries
#key:value
marks={'hindi':50, 'english':90}
print(type(marks))

#to reterive value faster
print(marks['hindi']) #you will get marks of hindi
print(marks['english'])

#use  .get for not to show error in code
print(marks.get('hindi'))
print(marks.get('maths')) #// error will not come

#to add value in variable
marks['maths']=100 #// [key]=value
print(marks)
print(marks.get('maths'))

#to delete
del marks['hindi']
print(marks)






