#Nested If else condition

#syntax

#//Example -1
age=20
voter_id =True
if age>=18:
    if voter_id:
        print('you can Vote')
    else:
        print('You need Voter id For Voting..')
else:
    print('You Can not Vote')


#example2
Vote=int(input('enter a age: '))

if Vote>=18:
    aadhar_card = True
    if aadhar_card:
        print('Elgible for Voting..')
    else:
        print('You need Voter id For Voting..')
else:
    print('Not eligible for Voting..')


    '''
    #// Nested if else used inside if else means you second time if else insided if else
    here 
    1- if one condition meet but another condtion Not meet then  else condition inside if condition will print 
    2- if both if condition meet then it print if condition
    3- if if outside condition not meet then outside else condition will print
    '''

