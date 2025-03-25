from datetime import datetime

###  CLASSES  ###
class Student:
    def __init__(self, num, fn, ln, dob, g, cy):
        self.__num = num
        self.__fn = fn
        self.__ln = ln
        self.__dob = datetime.strptime(dob, '%d-%m-%Y')
        self.__g = g          
        self.__cy = cy        

		# GET/SET STUDENT NUMBER
    def get_num(self):
        return self.__num
    def set_num(self, x):
        self.__num = x
        snum = str(self.__num)
        print ("Student number have been changed to " + snum)
		
    #GET/SET FIRST NAME
    def get_fn(self):
        return self.__fn
    def set_fn(self, x):   
        self.__fn = x
		
    #GET/SET LAST NAME
    def get_ln(self):
        return self.__ln    
    def set_ln(self, x):
        self.__ln = x
		
    #GET/SET DOB
    def get_dob(self):
        return self.__dob    
    def set_dob(self):     
        x = input("Enter your date of birth (DD-MM-YYYY): ")
        self.__dob = datetime.strptime(x, '%d-%m-%Y')

    #GET/SET GENDER
    def get_gen(self):
        return self.__g
    def set_gen(self, x):
        self.__g = x

    #GET/SET COUNTRY
    def get_country(self):
        return self.__cy
    def set_country(self, x):
        self.__country = x    

    #GET AGE
    def get_age(self):
        today = datetime.now()
        age = today.year - self.__dob.year - ((today.month, today.day) < (self.__dob.month, self.__dob.day))
        print(age)

### END OF CLASS ###




### FUNCTIONS ###


def export_students(student_list, filename="students.txt"):
    with open(filename, 'w') as file:
        for student in student_list:
            if student is not None:  
              # seperated by | for easier importing
                student_data = (
                    f"{student.get_num()}|"
                    f"{student.get_fn()}|"
                    f"{student.get_ln()}|"
                    f"{student.get_dob().strftime('%d-%m-%Y')}|"
                    f"{student.get_gen()}|"
                    f"{student.get_country()}\n"
                )
                file.write(student_data)
    print(f"Students exported to {filename}")



def import_students(filename="students.txt"):
    students = [None] * 100  
    try:
        with open(filename, 'r') as file:
            for i, line in enumerate(file):
                if i >= 100:  
                    break
                if line.strip():
                  #Split each line to 6 parts on |
                  #Creates "fields" a list/Array that contains the data. 
                    fields = line.strip().split('|')
                    #only accepts student data if all 6 fields are there
                    if len(fields) == 6:  
                        student = Student(
                            fields[0],  
                            fields[1],  
                            fields[2],  
                            fields[3],  
                            fields[4],  
                            fields[5]   
                        )
                        students[i] = student
        print(f"Students imported from {filename}")
        return students
      
    #Error handling
    except FileNotFoundError:
        print(f"File {filename} not found")
        return students
    except Exception as e:
        print(f"Error reading file: {str(e)}")
        return students

def show_student_data(student):
    print(f" Student Number:    {student.get_num()}")
    print(f" First Name:        {student.get_fn()}")
    print(f" Last Name:         {student.get_ln()}")
    print(f" Age:               {student.get_dob()}")
    print(f" Gender:            {student.get_gen()}")
    print(f" Country or Origin: {student.get_country()}")


def show_all_student_data(students):
    print("====== Dumping all available student data ======")
    for i, student in enumerate(students, start=1):
        print(f"Student {i}")
        show_student_data(student)
    # for each student in the student list
    # print out their: student number, first name, lastname, gender, age

def handle_exit():
    print("Quitting program .....")
    exit(0)

def modify_student_record(students):
    student_numbers = [str(student.get_num()) for student in students]
    chosen_number = input("Input student number for student whose record you want to modify\nMust be a number: ")
    while(chosen_number not in student_numbers and chosen_number != 'q'):
        print("Please enter a valid student number.\nYou can enter 'q' to quit or choose a proper number from those below:\n")
        for i, number in enumerate(student_numbers, start=1):
            print(f"{i}. {number}")
    if(chosen_number == 'q'):
        handle_exit()
    chosen_student = [std for std in students if std.get_num() == chosen_number][0]
    show_student_data(chosen_student)
    record_to_modify = input("Choose from the above which record you want to modify\n")

        
    

        
    
    pass
    # ask for which student to modify
    # confirm student is in list
    # ask for what needs to be modified (show what can be modified)
    # check if it is one of the properties 
    # modify student object in question and give feedback on how that went


###  END OF FUNCTIONS ###

def main():
    # main code to be run from here
    student_list = import_students()
    running = True
    while(running):
        print("=== FILE BASED STUDENT DATA MANAGEMENT APPLICATION ====")
        print("Available Features: ")
        print("1. Add new student to file ")
        print("2. Find student by student number and show all information stored on them")
        print("3. Show for each student, all data stored in data file")
        print("4. Show students that were born in a particular year")
        print("5. Modify student details for particular student")
        print("6. Delete student of choice from record (choose from available student numbers)")
        print("7. Quit the program")
        try:
            choice = int(input("What would you like to do?\n[Input number indicating your choice from the above mentioned]: "))
        except Exception as e:
            print("Please enter a valid choice [a single digit in the range 1-6]")
            exit(1)
        if(choice not in range(1,7)):
            print("Your choice is not available among the above listed. Please choose from the above listed options")
            exit(1)
        elif(choice == 1): # adding student to student file
            pass
        elif(choice == 2): # finding student by student number, displaying all their data
            pass
        elif(choice == 3): # for each student , list their data
            show_all_student_data(students=student_list)
        elif (choice == 4): # listing students born in a particular year  
            pass
        elif (choice == 5): # modify details for student number specified student
            pass
        elif (choice == 6): # delete student with specified student number
            pass 
        elif (choice == 7): # quit the program
            pass 


if __name__ == '__main__':
    main()








# student_list = [None] * 100


# # anything below is just for trying, all can be modified or removed
# student_list[0] = Student("001", "John", "Doe", "15-05-2000", "M", "USA")
# student_list[1] = Student("002", "Jane", "Smith", "22-08-2001", "F", "Canada")


# export_students(student_list)


# new_students = import_students()
    
# if new_students[0]:
#     print(f"Imported student: {new_students[0].get_fn()} {new_students[0].get_ln()}")