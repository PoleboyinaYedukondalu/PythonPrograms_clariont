## example prohram of multiple inheritance 
### written by nani (Yedukondalu Poleboyina)

# creating class
class main():
    def main_fun(self):
        Father_name="venkateswarlu"
        father_age=47
        print("my father name is :",Father_name)
        print("my father age is :",father_age)
class sub():
    def sub_fun(self):
        Mothetr_name="Lakshmi Kumari"
        Mother_age=40
        print("my mother name is :",Mothetr_name)
        print("my mother age is :",Mother_age)
class finall(main,sub): ##Inherited main class and sun class in finall class
    def finall_fun(self):
        son_name="nani"
        son_age=22
        print("my name is :",son_name)
        print("i am :",son_age," years old")

#object calling 
object_calling = finall()

#calling main_fun wchich present in the main class throug interited in finall class
object_calling.main_fun()

#calling sub_fun wchich present in the main class throug interited in finall class
object_calling.sub_fun()

#calling finall_fun wchich present in finall class
object_calling.finall_fun()