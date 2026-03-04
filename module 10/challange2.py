class DigitalSchool:
    def __init__(self, name, city, state, courses):
        self.__name = name
        self.__city = city
        self.__state = state
        self.__courses = courses

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, city):
        self.__city = city

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, state):
        self.__state = state

    @property
    def courses(self):
        return self.__courses

    @courses.setter
    def courses(self, courses):
        self.__courses = courses

    def show_school_info(self):
        return {
            "Name:": self.__name,
            "City:": self.__city,
            "State:": self.__state,
            "Courses:": self.__courses,
        }
    def organize_hackathon(self):
        print(f"Organize hackathon event")

class DS_Prishtina(DigitalSchool):
    def __init__(self, name, city, state, courses, student_number):
        super().__init__(name, city, state, courses)
        self.__student_number = student_number

    @property
    def student_number(self):
        return self.__student_number

    def SCF(self):
        print("Digital School Prishtina is organizing a Spring Code Fest(SCF)")

    def organize_hackathon(self):
        print("DS Prishtina is organizing a hackathon")

ds_prishtina = DS_Prishtina(
    name = "Digital School Prishtina",
    city = "Prishtina",
    state =  "Kosovo",
    courses= ["Python", "Js,HTML,CSS", "Wordpress"],
    student_number= 27
)
ds_prishtina.SCF()
ds_prishtina.organize_hackathon()

print(f"The number of student in DS prishtina is {ds_prishtina.student_number}")




