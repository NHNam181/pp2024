#Main
from domains.student import Student
from domains.course import Course

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
