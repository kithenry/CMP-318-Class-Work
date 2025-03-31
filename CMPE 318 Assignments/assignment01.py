from datetime import datetime

### GLOBALS  ###
date_format = "%d-%m-%Y"


###  CLASSES  ###
class Student:
    def __init__(self, student_number, first_name, last_name, dob, gender, country):
        self.__student_number = student_number
        self.__first_name = first_name
        self.__last_name = last_name
        self.__dob = datetime.strptime(dob, date_format)
        self.__gender = gender          
        self.__country = country        

	# GET/SET STUDENT NUMBER
    def get_student_number(self):
        return self.__student_number
    def set_student_number(self, x):
        self.__student_number = x
        updated_student_number = str(self.__student_number)
        print ("Student number have been changed to " + updated_student_number)
		
    #GET/SET FIRST NAME
    def get_first_name(self):
        return self.__first_name
    def set_first_name(self, x):   
        self.__first_name = x
        print(f"Student now has a new first name {self.get_first_name()}")
		
    #GET/SET LAST NAME
    def get_last_name(self):
        return self.__last_name    
    def set_last_name(self, x):
        self.__last_name = x
        print(f"Student now has a new last name: {self.get_last_name()}")
		
    #GET/SET DOB
    def get_dob(self):
        return self.__dob    
    def set_dob(self):     
        x = input("Enter your date of birth\nUse the format (DD-MM-YYYY): ")
        self.__dob = datetime.strptime(x, '%d-%m-%Y')
        print(f"Student now has a new DOB: {self.get_dob()}")

    #GET/SET GENDER
    def get_gender(self):
        return self.__gender
    def set_gender(self, x):
        self.__gender = x
        print(f"Student now has a new gender! Student is {self.get_gender()}")

    #GET/SET COUNTRY
    def get_country(self):
        return self.__country
    def set_country(self, x):
        self.__country = x    

    #GET AGE
    def get_age(self):
        today = datetime.now()
        age = today.year - self.__dob.year - ((today.month, today.day) < (self.__dob.month, self.__dob.day))
        return age

    #GET FULL NAME
    def get_full_name(self):
        return f"{self.get_first_name().capitalize()} {self.get_last_name().capitalize()}"

### END OF CLASS ###




### FUNCTIONS ###


def export_students(student_list, filename="students.txt"):
    with open(filename, 'w') as file:
        for student in student_list:
            if student is not None:  
              # seperated by | for easier importing
                student_data = (
                    f"{student.get_student_number()}|"
                    f"{student.get_first_name()}|"
                    f"{student.get_last_name()}|"
                    f"{student.get_dob().strftime(date_format)}|"
                    f"{student.get_gender()}|"
                    f"{student.get_country()}\n"
                )
                file.write(student_data)
    print(f"Student records successfully written to {filename}!")



def import_students(filename="students.txt"):
    students = [] # edited
    print("importing students")
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
                        students.append(student)
        print(f"Students imported from {filename}")
        return students
      
    #Error handling
    except FileNotFoundError:
        print(f"The file {filename} was not found")
        return students
    except Exception as e:
        print(f"Error reading file: {str(e)}")
        return students


def handle_exit():
    print("Alright.. quitting program .....")
    exit(0)

class StudentDatabase:
    def __init__(self):
        self.students = import_students()

    def add_student(self, student):
        if len(self.students) < 100:
            self.students.append(student)
            self.update_database()
        else:
            print("Oops! No space left. Student database is full :\\")

    def find_student_by_number(self, student_number):
        for student in self.students:
            if student.get_student_number() == student_number:
                return student
        return None

    def remove_student(self, student_number):
        student = self.find_student_by_number(student_number)
        if student:
            self.students.remove(student)
            print(f"Student with number {student_number} has been wiped from the records.")
            self.update_database()
        else:
            print(f"I think we don't have {student_number} in our records. Check that again.")
            print(f"You can choose main menu option five to select the desired student's number")

    def modify_student(self, student_number): # this was also kith's task but thanks again , heheeh
        student = self.find_student_by_number(student_number)
        fields = "first name, last name, date of birth, gender, country of birth".split(",")
        if student:
            print("Select field to modify:")
            print("1. First Name")
            print("2. Last Name")
            print("3. Date of Birth")
            print("4. Gender")
            print("5. Country of Birth")
            choice = input("Your choice must be integer in the range(1-5): ") # error check (try except block)
            run = True 
            while (run):
                if(choice == 'q'):
                    pass # handle quit
                if (choice not in '1 2 3 4 5'.split()):
                    print("[BAD INPUT!!\nInput must be an one of integers 1,2,3,4,5 from above]: ")
                    print("And... you may quit anytime by entering 'q'")
                    choice = input("Now try that again:[1,2,3,4,5] Go: ")
                    continue
                choice  = int(choice)
                run = False 
            
            new_value = input(f"Okay, noted.\nNow enter new {fields[choice-1]} value for {student.get_full_name()}: ")
            if choice == 1:
                student.set_first_name(new_value)
            elif choice == 2:
                student.set_last_name(new_value)
            elif choice == 3:
                student.set_dob(new_value)
            elif choice == 4:
                student.set_gender(new_value)
            elif choice == 5:
                student.set_country(new_value)
            
        else:
            print(f"Student with number {student_number} not found.")
    
    def show_student_data(self,student):
        print(f" Student Number:    {student.get_student_number()}")
        print(f" First Name:        {student.get_first_name()}")
        print(f" Last Name:         {student.get_last_name()}")
        print(f" Age:               {student.get_age()}")
        print(f" Gender:            {student.get_gender()}")
        print(f" Country or Origin: {student.get_country()}")

    def show_all_students(self): # this was kith's task but thanks.. hehee
        print()
        print("====== Retrieving all stored student data ======")
        if not self.students:
            print("Oops! there's no students stored!")
            print("You can add a new student entry via main menu option 3")
            print("You can also load your own student file via menu option 2")
        else:
            for i,student in enumerate(self.students, start=1):
                print(f"Student {i}")
                print()
                self.show_student_data(student)
                print()
                print()
            print("That's all of them...")

    def show_students_born_in_year(self, year):
        found = False
        for student in self.students:
            if student.get_dob().year == year:
                found = True
                print()
                print()
                self.show_student_data(student)
        if not found:
            print(f"No students born in the year {year}.")

    def read_from_file(self, filename):
        self.students = import_students(filename)
    # also functions as utility for writing to custom file
    def update_database(self, filename='students.txt'):
        export_students(self.students, filename)


def menu():
    global date_format
    db = StudentDatabase()
    run = True 
    while run:
        print("\nStudent Database Menu")
        print("1. Write to file")
        print("2. Read from file")
        print("3. Add a new student")
        print("4. Find student by number")
        print("5. Show all students")
        print("6. Show students born in a specific year")
        print("7. Modify student record")
        print("8. Delete a student")
        print("9. Exit")
        
        choice = input("Enter your choice: ")
        try:
            choice = int(choice)
        except Exception as e:
            print("You entered invalid input.\n Let's try that again")
            continue
        if choice == 1:
            filename = input("Enter filename to save to: ")
            db.update_database(filename=filename)
        elif choice == 2:
            filename = input("Enter filename to load from: ")
            db.read_from_file(filename)
        elif choice == 3:
            student_number = input("Enter student number: ")
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            date_of_birth = input("Enter date of birth (format: DD-MM-YY): ")
            gender = input("Enter gender (Database only supports Male or Female Genders :\\): ")
            country_of_birth = input("Enter country of birth: ")
            student = Student(student_number=student_number, first_name=first_name, last_name=last_name, dob=date_of_birth, gender=gender, country=country_of_birth)
            db.add_student(student)
        elif choice == 4:
            student_number = input("Enter student number to find: ")
            student = db.find_student_by_number(student_number)
            if student:
                print(student)
            else:
                print(f"Student with number {student_number} not found.")
        elif choice == 5:
            db.show_all_students()
        elif choice == 6:
            year = int(input("Enter the year: "))
            db.show_students_born_in_year(year)
        elif choice == 7:
            student_number = input("Enter student number to modify: ")
            db.modify_student(student_number)
        elif choice == 8:
            student_number = input("Enter student number to delete: ")
            db.remove_student(student_number)
        elif choice == 9:
            handle_exit()
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    menu()






