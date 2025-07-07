#object orineted project


#1- Classess
'''
employee1 = { 'name':'Raju',
              'email':'raju@gmail.com',
              'dept':'Devops',
              'salary':2300}
employee2 = {
    'name':'Kakshil',
    'email':'Kakshil@gmail.com',
    'dept':'Cloud',
    'salary':5300}
employee3 = {
    'name':'rohan',
    'email':'rohan@gmail.com',
    'dept':'CS',
    'salary':9000}
'''
from copyreg import constructor


#-----------------------------------------------------------------------------------------------------------------
class Employee:   #//employee --> class
    Company = 'Tech Mahindra.pvt.Ltd'
    def __init__(self,name,email,dept,salary):
        self.name=name
        self.email=email
        self.dept=dept
        self.salary=salary
    def emp_info(self):
        print("Name:",self.name)
        print("Email:",self.email)
        print("Dept:",self.dept)
        print("Salary:",self.salary)
    def change_dept(self,new_dept):
        self.dept=new_dept
        print(f'New Dept :{new_dept}')


emp01=Employee('raju','raju@email.com','sales',4000)   #emp01() ---> object
emp02=Employee('Kakshil','Kakshil@gmail.com','Cloud',5300)
print(emp01.Company)
emp01.emp_info()
emp01.change_dept('Cloud enginner')
emp01.emp_info()
print(emp02.Company)
emp02.emp_info()
emp02.change_dept('CS')
emp02.emp_info()



