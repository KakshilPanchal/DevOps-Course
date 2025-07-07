#reading and writing Files
#syntax
'''
with open('filename',w) as file:
file.write("hii my name is kakshil panchal")
'''

with open('New_file.txt','a')as file:
    file.write("kakshil panchal\ndwait vaidya")
    #1-  if we use 'w' then if we modify content then old content will replace with new content
    # 2- but if we use 'a' append means add content and exsiting content is been not removed

with open('New_file.txt','r') as file:
    #content=file.read()        #file content will print
    content=file.readlines()    #to read content line by line

for file in content:
    print(f'welcome {file.rstrip()}')  #.strip
