class Employee:
    def __init__(self,name,id,dept,sal):
        self.name=name
        self.id=id
        self.dept=dept
        self.sal=sal
    def updateSal(self,dept,sal):
        if(self.dept==dept):
            self.sal=sal
            
Emp=[]
n=int(input("enter the number of employees"))
for i in range(n):
    name=input("enter the name:")
    id=input("enter the id:")
    dept=input("enter the department:")
    sal=int(input("enter the salary:"))
    emp1=Employee(name,id,dept,sal)
    Emp.append(emp1)
print("Employee details are:")
for i in range(n):
    print(Emp[i].name," ",Emp[i].sal)
print("Updating the salary of particular department")
dept=input("enter the department whose salary has to be updated:")
sal=int(input("enter the salary to update:"))
for i in range(n):
    Emp[i].updateSal(dept,sal)
    print(Emp[i].name," ",Emp[i].sal)

            
    