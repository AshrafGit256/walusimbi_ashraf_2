class Person:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID

    def display_details(self):
        print(f'Name: {self.name}, ID: {self.ID}')


class Student(Person):
    def __init__(self, name, ID, program, cgpa):
        super().__init__(name, ID)
        self.program = program
        self.cgpa = cgpa

    def update_cgpa(self, new_cgpa):
        self.cgpa = new_cgpa
        print(f'{self.name}\'s CGPA updated to {self.cgpa}')

    def display_details(self):
        print(f'Student Name: {self.name}, ID: {self.ID}, Program: {self.program}, CGPA: {self.cgpa}')


class Lecturer(Person):
    def __init__(self, name, ID, department, courses):
        super().__init__(name, ID)
        self.department = department
        self.courses = courses 

    def assign_course(self, course):
        self.courses.append(course)
        print(f'New course "{course}" assigned to {self.name}')

    def display_details(self):
        print(f'Lecturer Name: {self.name}, ID: {self.ID}, Department: {self.department}, Courses: {self.courses}')


class Staff(Person):
    def __init__(self, name, ID, job_title, work_hours):
        super().__init__(name, ID)
        self.job_title = job_title
        self.work_hours = work_hours

    def update_work_hours(self, hours):
        self.work_hours = hours
        print(f'{self.name}\'s working hours updated to {self.work_hours} hours/week')

    def display_details(self):
        print(f'Staff Name: {self.name}, ID: {self.ID}, Job Title: {self.job_title}, Work Hours: {self.work_hours}/week')


student = Student("Ashraf", "230071466", "Software Engineering", 4.2)
lecturer = Lecturer("Dr. Swaib", "LEC001", "Computer Science", ["Python", "Machine Learning", "C", "C++"])
staff = Staff("Mr. Frank", "STF1001", "Librarian", 40)


print("\n--- STUDENT DETAILS ---")
student.display_details()
student.update_cgpa(4.5)

print("\n--- LECTURER DETAILS ---")
lecturer.display_details()
lecturer.assign_course("Java")

print("\n--- STAFF DETAILS ---")
staff.display_details()
staff.update_work_hours(35)
