# class ReportCard:
#     def __init__(self, name, **kwargs):
#         self.name = name  # string representing the student's name
#         self.grades = kwargs  # dict of course names and grades
#
#     def get_grade(self, course):
#         if course in self.grades:
#             return self.grades[course]
#         else:
#             return "No such grade..."
#
#     def print_all_grades(self):
#         for course, grade in self.grades.items():
#             print(f"{course}: {grade}")
#
#     def gpa(self):
#         return sum(self.grades.values()) / len(self.grades)
#
#
# rc = ReportCard("Ewa Barczykowska", Math=95, Science=85, English=90)  # passing as keyword arguments!
# # print(rc)
# # print(rc.name)
# # print(rc.grades)
# # print(rc.get_grade("French"))
# rc.print_all_grades()
# print(rc.gpa())

# reworked as per exercises from the course

class ReportCard:
    def __init__(self, name, **kwargs):
        self.name = name  # string representing the student's name
        self.grades = kwargs  # dict of course names and grades

    def __repr__(self):
        list_of_grades = [f"{course}: {grade}" for course, grade in self.grades.items()]
        return ", ".join(list_of_grades)

    def get_grade(self, course):
        if course in self.grades:
            return self.grades[course]
        else:
            return "No such grade..."

    # def print_all_grades(self): # replaced with __repr__ above
    #     for course, grade in self.grades.items():
    #         print(f"{course}: {grade}")

    def gpa(self):
        return sum(self.grades.values()) / len(self.grades)


# rc = ReportCard("Ewa Barczykowska", Math=95, Science=85, English=90)  # passing as keyword arguments!
# print(rc)
# print(rc.name)
# print(rc.grades)
# print(rc.get_grade("French"))
# print(rc)


# print(rc.gpa())

class LetterReportCard(ReportCard):
    def __init__(self, name, **kwargs):
        super().__init__(name, **kwargs)  # calling parent's constructor first!

        # self.name = name  # string representing the student's name
        # self.grades = {}

        for class_name, number_grade in kwargs.items():
            letter_grade = "F"
            if number_grade > 90:
                letter_grade = "A"
            elif number_grade > 80:
                letter_grade = "B"
            elif number_grade > 70:
                letter_grade = "C"
            elif number_grade > 60:
                letter_grade = "D"
            self.grades[class_name] = letter_grade

    def gpa(self):
        raise ValueError("Cannot calculate GPA for a LetterReportCard, not implemented yet.")


rc = LetterReportCard("Ewa Barczykowska", Math=95, Science=85, English=90)  # passing as keyword arguments!
print(rc.get_grade("Math"))
print(rc)
# print(rc.gpa())
