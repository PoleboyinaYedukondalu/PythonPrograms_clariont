#creating a class :
class Employee_details:
    emp_name="nani"
    emp_contact=9912542198
    company="clariont"
    role="Python Developer"

    def employee1(self):#,emp_name,emp_contact,company,role):
        # self.emp_namename="nani"
        # self.emp_contact=9912542198
        # self.company="clariont"
        # self.role="Python Developer"
        print("Employee Name :", self.emp_name)
        print("Employee Contact :", self.emp_contact)
        print("Employee company :", self.company)
        print("Employee Name :", self.role)

    def employee2(self,name,contact,company,role):
        self.name=name
        self.contact=contact
        self.company=company
        self.role=role
        print("Employee Name :", self.name)
        print("Employee Contact :", self.contact)
        print("Employee company :", self.company)
        print("Employee Name :", self.role)

#creating object1 for calling class get employee1 details :
emp_details=Employee_details()

#updating the employee details :
emp_details.emp_name = "pavan"
emp_details.emp_contact = 987654321
emp_details.company="Ekipit"
emp_details.role="Developer"
emp_details.employee1()

print("------------------------------------------")
#creating object2 for calling class get employee2 details :
emp_details2=Employee_details()
#calling the function in the class with passing the parameters :
emp_details2.employee2("Vijaya",123456789,"clariont","Azure")
print("------------------------------------------")
emp_details2.employee2("sai",876545678,"Ekipit","Java")
print("------------------------------------------")
emp_details2.employee2("Nani",9912542198,"Clariont","python")

