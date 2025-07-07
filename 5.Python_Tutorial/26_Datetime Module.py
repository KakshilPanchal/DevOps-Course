import datetime

# syntaz datetime.datetime.today --> datetime is module, datetime is class and .today is class method
a=datetime.datetime.today() #//it will show full format of date and time
print(a)

x=datetime.date.today() #// show only date
print(x)

y=datetime.datetime.today()
print(y.time())


# changing Fromatting or editing date or time usinf strftime
y=a.strftime('%Y=%m=%d %H-%M %h %m')
print(y)