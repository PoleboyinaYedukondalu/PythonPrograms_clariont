# overloading example
### writen by nani

def details(name,number,role=None):

    if role != None:
        print("my name is :",name)
        print("my contact number is :",number)
        print("my disignation is :",role)
    else:
        print("my name is :",name)
        print("my contact number is :",number)

details("nani",991542198,"python")
print("-----------------------------")
details("vijaya",8464845140)