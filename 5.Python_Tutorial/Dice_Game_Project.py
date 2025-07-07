############################# Dice Game Project #####################
import random
while True:


    flip=input('flip up Dice: ')
    if flip =='OK':   #If you flip up dice then Press Ok
        continue
    elif flip !='Ok': #Else if You dont Flip the dice then your turn is Gone and then you not get Number.
        print("your turn is Over due to take More Time..... ")
        break
    print(f"number is: {random.randint(1,6)}")  #random.randint will executed random numbers
    dice=input("Do you Want to continue? (y/n): ")
    '''
    if you want to continue to flip up dice and play game & get number again and again then press Y or if dont
     want to play dice game then press N so that you will exit from Dice Game.......
    '''
    if dice=='y':
        continue
    else:
        break