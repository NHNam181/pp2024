#Make OOP'ed

class Student: # Add Student class and use encapsulation
    def __init__(self, student_id, name, dob):
        self.ID = student_id
        self.Name = name
        self.DoB = dob
        self.Marks = {}

    def input_marks(self, courses):
        for course in courses:
            mark = float(input(f"Enter mark for {course.name}: "))
            self.Marks[course.name] = mark

    def display_info(self):
        print(f"\nID: {self.ID}\nName: {self.Name}\nDoB: {self.DoB}")
        print("Marks:")
        for course, mark in self.Marks.items():
            print(f"  {course}: {mark}")


class Course: # Add Course class and use encapsulation
    def __init__(self, name, course_id):
        self.name = name
        self.ID = course_id


def main():
    student_info = []
    course_info = []

    student_num = int(input("Input the number of students: "))
    for _ in range(student_num):
        student_id = input('Enter the student ID: ')
        name = input('Enter student name: ')
        dob = input('Enter student DoB: ')
        student_info.append(Student(student_id, name, dob))

    courses = int(input("Input the number of courses: "))
    for _ in range(courses):
        name = input('Enter course name: ')
        course_id = input('Enter course ID: ')
        course_info.append(Course(name, course_id))

    for student in student_info:
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