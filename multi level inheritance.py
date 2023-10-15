## simple example for multilevel inheritance :
### writen by Yedukondalu Poleboyina (Nani)

class father():
    def father_fun(self):
        Father_name="venkateswarlu"
        father_age=47
        print("my father name is :",Father_name)
        print("my father age is :",father_age)
class mother(father):
    def mother_fun(self):
        Mothetr_name="Lakshmi Kumari"
        Mother_age=40
        print("my mother name is :",Mothetr_name)
        print("my mother age is :",Mother_age)
class son(mother):
    def son_fun(self):
        son_name="nani"
        son_age=22
        print("my name is :",son_name)
        print("i am :",son_age," years old")

## calling sopn class with object
obj_calling=son()

## accesing father function
print("my father details :")
print("---------------------")
obj_calling.father_fun()
print("---------------------")
## accessing mother funtion
print("my mother details :")
print("---------------------")
obj_calling.mother_fun()
print("---------------------")

## accessing son function
print("my details :")
print("---------------------")
obj_calling.son_fun()
print("---------------------")


