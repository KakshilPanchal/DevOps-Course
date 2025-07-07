#string examples

a='   kakshil panchal, work in tech mahindra  '
b='second line'

#print(a.split(',')[0])

#print(a.split('panchal'))#//here panchal coubt as whitespace means it make whitespace between string by split
#means split break two string means make multiple string of one string
print(f'length of string: {len(a)}')
print(f'strip: {a.strip()}')  #remove whitespace
print(f'upper: {a.upper()}')
print(f'num: {a+b}')

num=1.0
num2=2.04
result=round(num+num2,1)
print(result)

#Abs command convert negative value into postive value
x=-10
y=10
res=abs(x)+(y)
print(res)
