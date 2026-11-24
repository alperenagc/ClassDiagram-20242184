# -*- coding: utf-8 -*-

class Student:
    def __init__(self, name: str, student_id: str, gpa: float = 0.0):
        # Attributes of the Student class
        self.name = name
        self.student_id = student_id
        self.gpa = gpa
        self.courses = []

    def add_course(self, course_name: str):
        """Adds a new course to the student's course list."""
        self.courses.append(course_name)
        print(f"Course '{course_name}' has been added for {self.name}.")

    def display_info(self):
        """Displays the student's details."""
        print("--- Student Information ---")
        print(f"Full Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print(f"GPA: {self.gpa}")
        print(f"Enrolled Courses: {', '.join(self.courses) if self.courses else 'No courses enrolled yet'}")

# --- Example Usage / Testing ---
if __name__ == "__main__":
    # Creating a Student object
    student1 = Student(name="John Doe", student_id="S2026001", gpa=3.45)
    
    # Calling methods
    student1.add_course("Object-Oriented Programming")
    student1.add_course("Data Structures")
    
    print()
    student1.display_info()