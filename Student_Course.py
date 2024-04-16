import random

class Student_Course:
    def __init__(self,
                 student_name=None,
                 age=None,
                 student_course=None,
                 level=None,
                 course=None,
                 subjects_semester_bscs=None,
                 schedule=None, professors=None,
                 subjects_semester_bsed=None,
                 subjects_semester_bsba=None,
                 bscs_prof=["Dr. Alejandro Santos", "Prof. Maria Cruz", "'Engr. Ricardo Fernandez", "Ms. Sofia Reyes"],
                 bsba_prof=["Dr. Miguel Dela Cruz", "Prof. Anna Lim", "Engr. Eduardo Reyes", "Ms. Isabella Gonzales"],
                 bsed_prof=["Dr. Sofia Ramirez", "Prof. Juan Santos", "Engr. Maria Garcia", "Ms. Josefa Hernandez"]):

        # Initialize class attributes
        self.course = course  # List of available courses
        self.subjects_semester_bscs = subjects_semester_bscs  # Subjects for BSCS
        self.subjects_semester_bsba = subjects_semester_bsba  # Subjects for BSBA
        self.subjects_semester_bsed = subjects_semester_bsed  # Subjects for BSED
        self.schedule = schedule  # Student's schedule
        self.professors = professors  # List of professors
        self.student_name = student_name  # Student's name
        self.age = age  # Student's age
        self.level = level  # Student's year level
        self.student_course = student_course  # Chosen course
        self.bscs_prof = bscs_prof  # Professors for BSCS
        self.bsba_prof = bsba_prof  # Professors for BSBA
        self.bsed_prof = bsed_prof  # Professors for BSED
        # Define available courses
        self.course = ["Bachelor of Science in Business Administration",
                       "Bachelor of Science in Computer Science",
                       "Bachelor of Science in Education"]

        # Define the subjects for BSCS, BSED, and BSBA
        self.subjects_semester_bscs = {
            1: {
                'Semester 1': ['Introduction to Programming', 'Mathematics for Computing', 'Digital Logic Design', 'Computer Fundamentals'],
                'Semester 2': ['Data Structures and Algorithms', 'Discrete Mathematics', 'Computer Organization and Architecture', 'Object-Oriented Programming']
            },
            2: {
                'Semester 1': ['Database Management Systems', 'Operating Systems', 'Web Development', 'Software Engineering'],
                'Semester 2': ['Computer Networks', 'Systems Analysis and Design', 'Algorithm Analysis', 'Human-Computer Interaction']
            },
            3: {
                'Semester 1': ['Advanced Data Structures', 'Computer Graphics', 'Software Testing and Quality Assurance', 'Artificial Intelligence'],
                'Semester 2': ['Machine Learning', 'Network Security', 'Cloud Computing', 'Mobile Application Development']
            },
            4: {
                'Semester 1': ['Software Project Management', 'Big Data Analytics', 'Computer Ethics and Society', 'Capstone Project'],
                'Semester 2': ['Internship', 'Cybersecurity', 'Parallel and Distributed Computing', 'Advanced Topics in Computer Science']
            }
        }

        self.subjects_semester_bsed = {
            1: {
                'Semester 1': ['Introduction to Education', 'Child Development', 'Educational Psychology', 'Teaching Methods'],
                'Semester 2': ['Curriculum Development', 'Assessment and Evaluation', 'Classroom Management', 'Education Technology']
            },
            2: {
                'Semester 1': ['Educational Research', 'Learning Theories', 'Literacy Education', 'Special Education'],
                'Semester 2': ['Mathematics Education', 'Science Education', 'Social Studies Education', 'Language Arts Education']
            },
            3: {
                'Semester 1': ['Educational Leadership', 'Counseling in Education', 'Inclusive Education', 'Teaching Practicum'],
                'Semester 2': ['Educational Policies', 'Diversity in Education', 'Global Education', 'Teaching Internship']
            },
            4: {
                'Semester 1': ['Professional Development Seminar', 'Education Law and Ethics', 'School Administration', 'Capstone Project'],
                'Semester 2': ['Student Teaching', 'Education Advocacy', 'Education Technology Integration', 'Advanced Topics in Education']
            }
        }

        self.subjects_semester_bsba = {
            1: {
                'Semester 1': ['Introduction to Business', 'Financial Accounting', 'Microeconomics', 'Business Communication'],
                'Semester 2': ['Managerial Accounting', 'Macroeconomics', 'Business Statistics', 'Marketing Principles']
            },
            2: {
                'Semester 1': ['Business Law', 'Corporate Finance', 'Operations Management', 'Management Information Systems'],
                'Semester 2': ['Human Resource Management', 'Business Ethics', 'Entrepreneurship', 'International Business']
            },
            3: {
                'Semester 1': ['Strategic Management', 'Organizational Behavior', 'Business Research Methods', 'Business Communication'],
                'Semester 2': ['Supply Chain Management', 'Financial Management', 'Project Management', 'Global Business']
            },
            4: {
                'Semester 1': ['Business Leadership', 'Risk Management', 'Business Innovation', 'Capstone Project'],
                'Semester 2': ['Internship', 'Business Negotiation', 'Corporate Social Responsibility', 'Advanced Topics in Business Administration']
            }
        }
    # Function to display the list of available courses and let the student choose    
    def student_courses(self):
        print("List of Coures:")
        x = 1
        for course in self.course:
            print(str(x)+"."+course)
            x += 1
        choice = input("Choose your Course:(1-3):")
        if choice == '1':
            self.student_course = self.course[0]
        elif choice == '2':
            self.student_course = self.course[1]
        elif choice == '3':
            self.student_course = self.course[2]  
                  
    # Function to gather student information    
    def student_info(self):
        while True:
           print("Enter your Information")
           self.student_name = input("Enter your Name:")
           self.age = input("Enter your Age:")   
           self.student_courses()
           self.level = input("Enter your year Level(1-4):")
           print()
           decision = input("Do you want to change information?(y) to proceed:")
           if decision.lower() == 'y':
               pass
           else:
               print()
               print("You are now Enrolled!")
               print("Student Information:")
               print("Name:",self.student_name)
               print("Age:",self.age)
               print("Year Level:",self.level)
               print("Course:",self.student_course)
               print()
               self.display_subjects()
               break
               
    # Function to display the subjects based on the chosen course and level          
    def display_subjects(self):
        level = int(self.level)
        course = self.student_course
        print("Your Subjects:")
        if course == "Bachelor of Science in Business Administration":
            if level == 1:
                sem1 = self.subjects_semester_bsba[level]['Semester 1']
                sem2 = self.subjects_semester_bsba[level]['Semester 2']
                print("First Semester:",sem1)
                print("Second Semester:",sem2)
                self.student_schedule(sem1,sem2)
            elif level == 2:
                sem1 = self.subjects_semester_bsba[level]['Semester 1']
                sem2 = self.subjects_semester_bsba[level]['Semester 2']
                print("First Semester:",sem1)
                print("Second Semester:",sem2)
                self.student_schedule(sem1,sem2)
            elif level == 3:
                sem1 = self.subjects_semester_bsba[level]['Semester 1']
                sem2 = self.subjects_semester_bsba[level]['Semester 2']
                print("First Semester:",sem1)
                print("Second Semester:",sem2)
                self.student_schedule(sem1,sem2)
            elif level == 4:
                sem1 = self.subjects_semester_bsba[level]['Semester 1']
                sem2 = self.subjects_semester_bsba[level]['Semester 2']
                print("First Semester:",sem1)
                print("Second Semester:",sem2)
                self.student_schedule(sem1,sem2)
            
        elif course == "Bachelor of Science in Computer Science":
            if level == 1:
                sem1 = self.subjects_semester_bscs[level]['Semester 1']
                sem2 = self.subjects_semester_bscs[level]['Semester 2']
                print("First Semester:",sem1)
                print("Second Semester:",sem2)
                self.student_schedule(sem1,sem2)
            elif level == 2:
                sem1 = self.subjects_semester_bscs[level]['Semester 1']
                sem2 = self.subjects_semester_bscs[level]['Semester 2']
                print("First Semester:",sem1)
                print("Second Semester:",sem2)
                self.student_schedule(sem1,sem2)
            elif level == 3:
                sem1 = self.subjects_semester_bscs[level]['Semester 1']
                sem2 = self.subjects_semester_bscs[level]['Semester 2']
                print("First Semester:",sem1)
                print("Second Semester:",sem2)
                self.student_schedule(sem1,sem2)
            elif level == 4:
                sem1 = self.subjects_semester_bscs[level]['Semester 1']
                sem2 = self.subjects_semester_bscs[level]['Semester 2']
                print("First Semester:",sem1)
                print("Second Semester:",sem2)
                self.student_schedule(sem1,sem2)
        
        elif course == "Bachelor of Science in Education":
            if level == 1:
                sem1 = self.subjects_semester_bsed[level]['Semester 1']
                sem2 = self.subjects_semester_bsed[level]['Semester 2']
                print("First Semester:",sem1)
                print("Second Semester:",sem2)
                self.student_schedule(sem1,sem2)
            elif level == 2:
                sem1 = self.subjects_semester_bsed[level]['Semester 1']
                sem2 = self.subjects_semester_bsed[level]['Semester 2']
                print("First Semester:",sem1)
                print("Second Semester:",sem2)
                self.student_schedule(sem1,sem2)
            elif level == 3:
                sem1 = self.subjects_semester_bsed[level]['Semester 1']
                sem2 = self.subjects_semester_bsed[level]['Semester 2']
                print("First Semester:",sem1)
                print("Second Semester:",sem2)
                self.student_schedule(sem1,sem2)
            elif level == 4:
                sem1 = self.subjects_semester_bsed[level]['Semester 1']
                sem2 = self.subjects_semester_bsed[level]['Semester 2']
                print("First Semester:",sem1)
                print("Second Semester:",sem2)
                self.student_schedule(sem1,sem2)
    
     # Function to generate and display the student's schedule
    def student_schedule(self,sem1,sem2):
        course = self.student_course
        if course == "Bachelor of Science in Business Administration":
            profs = self.bsba_prof[:4]
        elif course == "Bachelor of Science in Computer Science":
            profs = self.bscs_prof[:4]
        elif course == "Bachelor of Science in Education":
            profs = self.bsed_prof[:4]
            
        random_numberm1 = random.choice([0, 2])
        random_numbert1= random.choice([1, 3])
        random_numberm2 = random.choice([0, 2])
        random_numbert2 = random.choice([1, 3])
        print("Schedule:")
        print("First Semester:")
        self.date_plan(sem1[0],sem1[1],sem1[2],sem1[3],profs[random_numberm1],profs[random_numbert1],profs[random_numberm2],profs[random_numbert2])
        print()
        print("Second Semester:")
        self.date_plan(sem2[0],sem2[1],sem2[2],sem2[3],profs[random_numberm2],profs[random_numbert2],profs[random_numberm1],profs[random_numbert1])
        
    # Function to format and print the schedule for each day 
    def date_plan(self,sub1,sub2,sub3,sub4,m1_prof,m2_prof,tu1_prof,tu2_prof):
        print("Monday") 
        print("7:00am to 9:30am:","Subject:",sub1,"|","Prof:",m1_prof)
        print("9:30am to 12:00pm:","Subject:",sub2,"|","Prof:",m2_prof)
        print("Tuesday")
        print("7:00am to 9:30am:","Subject:",sub3,"|","Prof:",tu1_prof)
        print("9:30am to 12:00pm:","Subject:",sub4,"|","Prof:",tu2_prof)
        print("Wednesday")
        print("7:00am to 9:30am:","Subject:",sub1,"|","Prof:",m1_prof)
        print("9:30am to 12:00pm:","Subject:",sub2,"|","Prof:",m2_prof)
        print("Thursday")
        print("7:00am to 9:30am:","Subject:",sub3,"|","Prof:",tu1_prof)
        print("9:30am to 12:00pm:","Subject:",sub4,"|","Prof:",tu2_prof)
        
    # Main function to start the enrollment process    
    def main_start(self):
        print("Student Course Enrollment App")
        self.student_info()  
         
    
# Create an instance of the Student_Course class and start the enrollment process
s = Student_Course()
s.main_start()
