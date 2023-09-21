#Storing Student Data in file using File handling Concept :
#Written by Yedukondalu

#defin a function of Adding Student Data :
def add_student():
    student_name = input("Enter student name: ")
    student_id = input("Enter student ID: ")
    student_class = input("Enter student class: ")
    Subject1_Marks = int(input("Enter Subject1 marks :"))
    Subject2_marks = int(input("Enter Subject2 marks :"))
    Subject3_Marks = int(input("Enter Subject3 marks :"))
    student_grade = ""

#Total  Student Marks :
    Total=Subject1_Marks+Subject2_marks+Subject3_Marks
    per=Total/3
    
#Student Grade Check :    
    if per>=90:
      student_grade="A+"
    elif per>=80:
     student_grade = "A"
    elif per>=70:
      student_grade = "B+"
    elif per>=60:
        student_grade = "B"
    elif per>=40:
        student_grade = "C"
    else:
        student_grade = "Fail"
    

#Assigning All inputs in a sigle variable using format key word (f"") :
    studentData = f"Student name :{student_name}, \n" \
        f"Student Id :{student_id}, \n" \
        f"Student Class :{student_class}, \n" \
        f"M1 Marks :{Subject1_Marks}, \n" \
        f"Subject2 Marks :{Subject2_marks}, \n" \
        f"Subject3 Marks :{Subject3_Marks}, \n" \
        f"Total :{Total}, \n" \
        f"Persentage :{per}, \n" \
        f"Student Grade :{student_grade} \n"

#Open a file with append and read mode (a+) :
    file=open("d:\\Files\\task.txt", "a+")
    file.write(studentData)
    file.close()
    
    print("Student data has been added successfully!")  


#Defining a function for itaration of adding student data : 
def itarator():
    while True:
        print("choose your option :")
        print("1. Add Student Data")
        print("2. Exit")
        
        choose = input("Enter your choice: ")

        if choose == "1":
            add_student()
        elif choose == "2":
            break
        else:
            print("Invalid choice. Please try again.")

#Calling itaration Function :
itarator()
