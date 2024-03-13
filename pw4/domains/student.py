import numpy as np

class Student:
    def __init__(self, student_id, name, dob):
        self.ID = student_id
        self.Name = name
        self.DoB = dob
        self.Marks = {}
        self.Credits = {}

    def input_marks(self, courses):
        for course in courses:
            mark = float(input(f"Enter mark for {course.name}: "))
            self.Marks[course.name] = math.floor(mark)

    def input_credits(self, courses):
        for course in courses:
            credit = int(input(f"Enter credits for {course.name}: "))
            self.Credits[course.name] = credit

    def calculate_gpa(self):
        total_credits = sum(self.Credits.values())
        weighted_marks = np.array([self.Marks[course] * self.Credits[course] for course in self.Marks])
        gpa = np.sum(weighted_marks) / total_credits
        return gpa

    def display_info(self):
        print(f"\nID: {self.ID}\nName: {self.Name}\nDoB: {self.DoB}")
        print("Marks:")
        for course, mark in self.Marks.items():
            print(f"  {course}: {mark}")
        print("Credits:")
        for course, credit in self.Credits.items():
            print(f"  {course}: {credit}")
        print(f"Average GPA: {self.calculate_gpa():.2f}")
