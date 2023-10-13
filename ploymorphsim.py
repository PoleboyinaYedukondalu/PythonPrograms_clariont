## example for ploymorphsim 
### writen by nani

class parent():
    def __init__(self,name,contact,company="clariont"):
        self.name=name
        self.contact=contact
        self.company=company
        print("parent Name :", self.name)
        print("parent Contact :", self.contact)
        print("parent company :", self.company)
class chaild(parent):
    def parentemployee1():
        super.__init__(self,name,contact)   
    def employee1(self,name,contact):
        self.name=name
        self.contact=contact
        print("chaild Name :", self.name)
        print("chaild Contact :", self.contact)

obj1=chaild()
obj1.employee1("nani",8464845140)
obj1.parentemployee1("nani",9912542198,"clariont")



