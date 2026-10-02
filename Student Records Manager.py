student_records={}

def add_student(name,age,courses):
    if name in student_records:
        print(f"Student '{name}' already exists.")
    else:
        student_records[name]= {}
        student_records[name]["age"]=age
        student_records[name]["grades"]= set()
        student_records[name]["courses"]= courses
        print(f"Student '{name}' added successfully.")

def is_enrolled(name,course):
    if name not in student_records:
        print(f"Student '{name}' not found.")
        
    else:
        if course in student_records[name]["courses"]:
            print(f"Yes, '{name}' is taking {course}. ")
        else:
            print(f"No, '{name}' is not taking {course}. ")

def add_grade(name,grades):
    if name not in student_records:
        print(f"Student '{name}' not found.")  
    else:
        student_records[name]["grades"].add(grades)
        print(f"Grade {grades} added for student '{name}'.")

def calculate_average_grade(name):
    if name not in student_records:
        print(f"Student '{name}' not found.")
    else:
        total_grades=0
        if student_records[name]["grades"]==set():
            print("Grades not entered. ")
        else:
            for i in student_records[name]["grades"]:
                total_grades+=i
            average_grade=total_grades/len(student_records[name]["grades"])
            print(f"The Average Grade of '{name}' is {average_grade}. ")
def list_students_by_course(course):
    list_by_course=[]
    for names_of_students in student_records:
        if course in student_records[names_of_students]["courses"]:
            list_by_course.append(names_of_students)
    print(f"Here is the list of students taking {course}: {list_by_course}")

def filter_top_students(threshold):
    list_of_top_students=[]
    for student in student_records:
        if student_records[student]["grades"]==set():
            continue
        else:
            total_grades=0
            for i in student_records[student]["grades"]:
                total_grades+=i
        average_grade=total_grades/len(student_records[student]["grades"])
        if average_grade > threshold:
            list_of_top_students.append(student)
    print(f"The list of Top students is: {list_of_top_students}")


add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Math", "Biology"])
add_student("Diana", 23, ["Chemistry", "Physics"])
add_grade("Alice", 90)
add_grade("Alice", 85)
add_grade("Bob", 75)
add_grade("Diana", 95)
filter_top_students(80) # Should return ["Alice", "Diana"]
filter_top_students(90)  # Should return ["Diana"]
filter_top_students(100)  # Should return an empty list