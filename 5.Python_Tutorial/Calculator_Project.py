#calculator Project

def add(x , y):
    return x + y
def subtract(x , y):
    return x - y
def divide(x, y):
    return x / y
def multiply(x , y):
    return x * y
def even_or_odd(x):
    if x % 2 == 0:
        return True
    else:
        return False

cont='y'
while cont.lower() == 'y':
    print("select operation\n1.Add \n2.substraction \n3.division \n4.multiply \n5.even_or_odd")
    choice = input("enter your choice:(1,2,3,4,5) ")
    num1=int(input("enter first number:"))
    num2=int(input("enter second number:"))

    if choice == '1':
        print(num1,"+",num2,"=", add(num1,num2))
    elif choice == '2':
        print(num1,"-",num2,"=",subtract(num1,num2))
    elif choice == '3':
        print(num1 ,"/",num2,"=",divide(num1,num2))
    elif choice == '4':
        print(num1,"*",num2,"=",multiply(num1,num2))
    elif choice == '5':
        print(num1,num2,"=",even_or_odd(num1,num2))
    else:
      print('invalid input')
    cont=input("continue?(y/n):")
    if cont == 'y':
         break


