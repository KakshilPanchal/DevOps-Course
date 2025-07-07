from logging import exception

#try --> error in code or issue in code is written in try section
# except --> and except will run when there is error found  in try section
#finally --> this will run complusory even error is there or not

#---> suppose i have build application and there is some bug in that application then due to that bug my application will not
# stop if we use try and exception handling case so that our application will run continously even bug is found.

#example
try:
 with open("New_file.txt") as file:
     content=file.readlines()
#except FileNotFoundError:
    #print("File not found")
except  Exception as e:
    print(e)
    print(type(e)) #//this use when you dont know type of  error will come or not then you use ----> Exception as e:
else:
    for read in content:
        print(f'welcome {read.rstrip()}')
finally: #// this operation will execute complusory..
    print('DATABASE END.......')


