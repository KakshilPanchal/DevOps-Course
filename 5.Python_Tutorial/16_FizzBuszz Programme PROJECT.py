'''
# Questions:-
1- programme should add number from 1 to a specified number in list
2- multiples of 3 it should be "fizz"
3- for multiples of 5 it should be "buzz"
4- for number multiples of both 3 and 5 it should be "fizzbuzz"
5- print the list
'''

#//Answer//

list_num=int(input("Enter the number: "))

for i in range(1, list_num+1):
    if i % 3 == 0 and i % 5 == 0:
        print(f'{i} Fizz Buzz')
    elif i % 3 == 0:
        print(f'{i} fizz')
    elif i % 5 == 0:
        print(f'{i} Buzz ')
    else:
        print(i)


