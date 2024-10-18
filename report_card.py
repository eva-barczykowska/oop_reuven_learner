class ReportCard:
    def __init__(self, name, **kwargs):
        self.name = name  # string representing the student's name
        self.grades = kwargs  # dict of course names and grades

    def get_grade(self, course):
        if course in self.grades:
            return self.grades[course]
        else:
            return "No such grade..."

    def print_all_grades(self):
        for course, grade in self.grades.items():
            print(f"{course}: {grade}")

    def gpa(self):
        return sum(self.grades.values()) / len(self.grades)


rc = ReportCard("Ewa Barczykowska", Math=95, Science=85, English=90)  # passing as keyword arguments!
# print(rc)
# print(rc.name)
# print(rc.grades)
# print(rc.get_grade("French"))
rc.print_all_grades()
print(rc.gpa())