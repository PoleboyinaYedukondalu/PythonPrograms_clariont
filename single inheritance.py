## simple example for single inheritance 
### writen by Yedukondalu Poleboyina (nani)

class parent():
    def parent_fun(self,Father_name,F_age):
        self.Father_name=Father_name
        self.F_age=F_age
        print("father name is :",self.Father_name)
        print("father age is :",self.F_age)
class chaild(parent):
    def chail_fun(self,Chaild_name,C_age):
        self.Chaild_name=Chaild_name
        self.C_age=C_age
        print("chaild name is :",self.Chaild_name)
        print("chaild age is :",self.C_age)

object_calling = chaild()
object_calling.parent_fun("venkateswarlu",47)
print("------------------------------------------")
object_calling.chail_fun("nani",22)
