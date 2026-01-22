class Course:
    def __init__ (self, course_name: str, course_grade: int, course_credits_number: int):
        self.course_name = course_name
        self.course_grade = course_grade
        self.course_credits_number = course_credits_number
    
    def get_course_name (self):
        return self.course_name
    
    def get_course_grade (self):
        return self.course_grade 
    
    def get_course_credits_number (self):
        return self.course_credits_number
    
class CourseCredits:
    def __init__ (self):
        self.__courses = {}
    
    def add_course (self, name: str, grade: int, credits_number: int):
        course_added = Course(name, grade, credits_number)
        self.__courses[name] = course_added
    
    def all_courses (self, course_name):
        courses = {}
        for name, course in self.__courses.items():
            courses[name] = [course.get_course_grade(), course.get_course_credits_number()]
            
        for key, value in courses.items():
            if course_name in key:
                if int(value[0]) < 13 and int(value[0]) > 8:
                    return key + "(" + str(value[1]) + " cr) grade " + str(value[0])
        return None
        
    def number_of_completed_courses(self):
        return len(self.__courses)
    
    def get_total_credits(self):
        total_credits = 0
        for name, course in self.__courses.items():
            total_credits = total_credits + int(course.course_credits_number)
        return total_credits
    
    def get_average_credits(self):
        total_credits = 0
        for name, course in self.__courses.items():
            total_credits = total_credits + int(course.course_credits_number)
            
        if len(self.__courses) > 0:
            average_credits = total_credits / len(self.__courses)
            return average_credits
        else:
            return 0
    
    def grade_distribution(self):
        ninth_grade_courses = 0
        tenth_grade_courses = 0
        eleventh_grade_courses = 0
        twelfth_grade_courses = 0
        
        for name, course in self.__courses.items():
            if course.course_grade == "9":
                ninth_grade_courses += 1 
                
            elif course.course_grade == "10":
                tenth_grade_courses += 1
            
            elif course.course_grade == "11":
                eleventh_grade_courses += 1 
            
            elif course.course_grade == "12":
                twelfth_grade_courses += 1 
        
        return "9th:" + str(ninth_grade_courses) + "\n" + "10th:" + str(tenth_grade_courses) + "\n" + "11th:" + str(eleventh_grade_courses) + "\n" + "12th:" + str(twelfth_grade_courses)
        
class CourseCreditsApplication:
    def __init__ (self):
        self.__course_catalog = CourseCredits()
    
    def directions (self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")
        
    def add_course_entry (self):
        name = input("name:")
        name_lower = name.lower()
        grade = input("grade:")
        credits = input("credits:")
        self.__course_catalog.add_course(name_lower, grade, credits)
    
    def get_course_data (self):
        name = input("name:")
        name_lower = name.lower()
        print(self.__course_catalog.all_courses(name_lower))
    
    def statistics (self):
        credit_total = self.__course_catalog.get_total_credits()
        course_total = self.__course_catalog.number_of_completed_courses()
        credit_average = self.__course_catalog.get_average_credits()
        distribution_of_grades = self.__course_catalog.grade_distribution()
        print(str(course_total), "completed courses, a total of", str(credit_total), "credits" )
        print("mean", str(credit_average))
        print("grade distribution:")
        print(distribution_of_grades)
        
        
    def execute(self):
        self.directions()
        while True:
            command = input("command: ")
            if command == '0':
                break
            elif command == '1':
                self.add_course_entry()
            elif command == '2':
                self.get_course_data()
            elif command == '3':
                self.statistics()
            else:
                self.directions()
        
application = CourseCreditsApplication()
application.execute()            
    
