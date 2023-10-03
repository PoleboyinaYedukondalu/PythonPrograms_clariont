''' public
    private __
    protected _
'''
class ScopeTest():
   def __init__(self,name,number,contact):
      self.contact=contact
      self.__name=name
      self._number=number
      
      print("name is :",self.__name) #private variabler can acces only with in the class
      print("number is :",self._number) 

class second(ScopeTest):
   def output(self):
      # print("parent name is :",self.__name) #we could not access pravite variables in chaild class
      print("parent roll number is :",self._number) # we can access protected variables in chaild class if we mention __init__ constaructor in the parent class, if we dont metion __init__ we can't access
      print("contact number is :",self.contact) #we can access public variables any where in the file 

obj=second("nani",5,9912542198)
obj.output()
      