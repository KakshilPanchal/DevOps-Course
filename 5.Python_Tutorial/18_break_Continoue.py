#break
#to stop loop
'''
     num = [1, 2,3, 4, 5, 6]
for n in num:
 if n >= 3:
    print(n)
    break
    #continue
 else:
     print("not Greater than 0 ")
     '''


#break
# if condition meet then remaining condition skip and again loop start

#example2
users=["sneha"]
name=''
while True:
    name=input('enter a Name: ')
    if name == 'exit':
        print('You are Exited....!!!!')
        break
    if name in users:
        print(f'User Account: {name} is Exist..')
        continue
    else:
      print(f'This type of User Account Not Exist...')


