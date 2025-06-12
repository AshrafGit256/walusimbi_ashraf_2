class UniversityStaff:
    def duty(self):
        print("University staff contribute to university operations.")

class Lecturer(UniversityStaff):
    def duty(self):
        print("Lecturer teaches university courses.")

class Researcher(UniversityStaff):
    def duty(self):
        print("Researcher conducts academic research.")

class Professor(Lecturer, Researcher):
    pass

p = Professor()
p.duty()
