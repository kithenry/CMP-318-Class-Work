from datetime import datetime

class student:
    def __init__(self, num, fn, ln, dob, g, cy):
        self.__num = num
        self.__fm = fn
        self.__ln = ln
        self.__dob = datetime.strptime(dob, '%d-%m-%Y')
        self.__g = g          
        self.__cy = cy        


    def get_num(self):
        return self.__num
    def set_num(self, x):
        self.__num = x
        snum = str(self.__num)
        print ("Student number have been changed to " + snum)
    def set_fn(self, x):   
        self.__fn = x
    def set_ln(self, x):
        self.__ln = x
    def set_dob(self):     #sets bday
        x = input("Enter your date of birth (DD-MM-YYYY): ")
        self.__dob = datetime.strptime(x, '%d-%m-%Y')
    def set_g(self, x):
        self.__g = x
    def set_country(self, x):
        self.__country = x    

    def get_age(self):
        today = datetime.now()
        age = today.year - self.__dob.year - ((today.month, today.day) < (self.__dob.month, self.__dob.day))
        print(age)

#end of class


std_list = []

