import pickle
import threading
from threading import Lock
from domains.student import Student
from domains.course import Course

class BackgroundThread(threading.Thread):
    def __init__(self, target, args=()):
        super().__init__()
        self.target = target
        self.args = args

    def run(self):
        self.target(*self.args)

class PicklePersistenceThread(BackgroundThread):
    def __init__(self, data, filename):
        super().__init__(target=self.save_pickle, args=(data, filename))
        self.data = data
        self.filename = filename
        self.lock = Lock()

    def save_pickle(self, data, filename):
        with self.lock:
            with open(filename, "wb") as file:
                pickle.dump(data, file)

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

    students_thread = PicklePersistenceThread(student_info, "students.pickle")
    courses_thread = PicklePersistenceThread(course_info, "courses.pickle")
    students_thread.start()
    courses_thread.start()

    students_thread.join()
    courses_thread.join()

    print("\nStudent Information:")
    for student in student_info:
        student.display_info()

    print("\nCourse Information:")
    for course in course_info:
        print(f"\nCourse Name: {course.name}\nCourse ID: {course.ID}")

    with open("students.pickle", "wb") as students_file:
        pickle.dump(student_info, students_file)

    with open("courses.pickle", "wb") as courses_file:
        pickle.dump(course_info, courses_file)

    with open("students.txt", "w") as students_file:
        for student in student_info:
            students_file.write(f"{student.ID}.{student.Name} - {student.DoB}\n")

    with open("courses.txt", "w") as courses_file:
        for course in course_info:
            courses_file.write(f"{course.ID}.{course.name}\n")

    with open("marks.txt", "w") as marks_file:
        for student in student_info:
            for course in course_info:
                marks_file.write(f"{student.ID}.{student.Name}:{course.name} - {student.Marks[course.name]}\n")

if __name__ == "__main__":
    main()
