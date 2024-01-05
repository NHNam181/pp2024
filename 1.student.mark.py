student_info = []
course_info = []

student_num = int(input("Input the number of students: "))

for i in range(student_num):
    student = {}
    student['ID'] = input('Enter the student ID: ')
    student['Name'] = input('Enter student name: ')
    student['DoB'] = input('Enter student DoB: ')
    
    # Store student's mark in each course
    student['Marks'] = {}
    
    student_info.append(student)

courses = int(input("Input the number of courses: "))

for i in range(courses):
    course = {}
    course['Course name'] = input('Enter course name: ')
    course['Course ID'] = input('Enter course ID: ')
    
    course_info.append(course)

#Print the student mark in the course
for student in student_info:
    print(f"\nEnter marks for student {student['Name']}:")
    for course in course_info:
        mark = float(input(f"Enter mark for {course['Course name']}: "))
        student['Marks'][course['Course name']] = mark

# Print the information
print("\nStudent Information:")
for student in student_info:
    print(f"\nID: {student['ID']}\nName: {student['Name']}\nDoB: {student['DoB']}")
    print("Marks:")
    for course, mark in student['Marks'].items():
        print(f"  {course}: {mark}")

print("\nCourse Information:")
for course in course_info:
    print(f"\nCourse Name: {course['Course name']}\nCourse ID: {course['Course ID']}")
