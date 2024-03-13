#Add floor()
#Use numpy module and its array to calculate GPA

import math
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

    def calculate_gpa(self): #Add caclulate_gpa function
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


class Course:
    def __init__(self, name, course_id):
        self.name = name
        self.ID = course_id


def main():
    student_info = []
    course_info = []

    student_num = int(input("\nInput the number of students: "))
    for _ in range(student_num):
        student_id = input('\nEnter the student ID: ')
        name = input('Enter student name: ')
        dob = input('Enter student DoB: ')
        student_info.append(Student(student_id, name, dob))

    courses = int(input("\nInput the number of courses: "))
    for _ in range(courses):
        course_id = input('Enter course ID: ')
        name = input('Enter course name: ')
        course_info.append(Course(name, course_id))

    for student in student_info:
        print(f"\nEnter credits for courses earned by Student {student.Name}:")
        student.input_credits(course_info)
        print(f"\nEnter marks for student {student.Name}:")
        student.input_marks(course_info)

    print("\nStudent Information:")
    for student in student_info:
        student.display_info()

    print("\nCourse Information:")
    for course in course_info:
        print(f"\nCourse Name: {course.name}\nCourse ID: {course.ID}")


if __name__ == "__main__":
    main()
