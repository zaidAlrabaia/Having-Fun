from PythonFundamentals import squared as s
a = s(12)
print(a )
class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
    
    def get_info(self):
        return self.name + " " + str(self.age) + " " + self.email

class Student (Person):
    def __init__(self, name, age, email, student_id):
        super().__init__(name, age, email)
        self.student_id = student_id
        self.courses = []
    
    def enroll(self, course):
        self.courses.append(course)
    
    def get_courses(self):
        return self.courses

class Teacher(Person):
    def __init__(self, name, age, email, teacher_id):
        super().__init__(name, age, email)
        self.courses = []
        self.teacher_id = teacher_id

    def assign_course (self, course):
        self.courses.append(course)
    
    def get_courses_taught(self):
        return [course.course_name for course in self.courses ]


class Course:
    def __init__(self, course_id, course_name):
        self.teacher = None
        self.students: list[Student] =  []
        self.course_id = course_id
        self.course_name = course_name
    
    def add_Student(self, Student):
        self.students.append(Student)
    def get_roster(self):
        return [self.name for student in self.students]

class School:
    def __init__(self, name, students, teachers, courses):
        self.name = name
        self.students: list[Student] = []
        self.teachers: list[Teacher] = []
        self.courses: list[Course] = []
    
    def add_student(self, student: Student):
        self.students.append(student)
    
    def add_teacher(self, teacher: Teacher):
        self.teachers.append(teacher)
    
    def add_course(self, course: Course):
        self.courses.append(course)
    
    def find_student_by_id(self, student_id):
        return [student for student in self.students if student.student_id == student_id]
    
    def find_teacher_by_id (self, teacher_id):
        return [teacher for teacher in self.teachers if teacher.teacher_id == teacher_id]
    
    def find_course_by_id(self, course_id):
        return[course for course in self.courses if course.course_id == course_id]
    
    def assign_teacher_to_course(self, teacher_id, course_id):
        teacher = self.find_teacher_by_id(teacher_id)     
        course = self.find_course_by_id(course_id)
        course.teacher = teacher
    
    def enroll_student_in_course(self,student_id,course_id):
        student = self.find_student_by_id(student_id)
        course = self.find_course_by_id(course_id)
        course.students.append(student)







