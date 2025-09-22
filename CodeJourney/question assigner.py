
# A program for identifying the questions randomly that each student should solve.
import random, time


def greet():
        #A fuction that define the program
        print()
        print(" Welcome to my program! ".center(40, '='))
        time.sleep(1)
        print("This program identify the questions randomly that each student should solve.\n")
        time.sleep(0.7)


def questions():
        #The count of questions and shuffle them
	while True:
        	try:
        		total = int(input("Enter the amount of the questions: "))
        		break
        	except ValueError:
        		print("Please only enter a number!")
	questions = list(range(1, total + 1))
	random.shuffle(questions)

	return questions, total


def get_students():
        #A function that takes the names of students
        students = []
        x = 1
        while True:
                student_name = input(f"\nEnter the student {str(x)} name (type stop to finish): ").capitalize()
                x += 1

                if student_name.lower() == 'stop':
                        break
                else:
                        students.append(student_name)

        print("Students: ")
        for student in students:
                print(' - ' + student)
                time.sleep(0.6)

        return students



def identify(students, questions, total):
        #A funtion that decideds which person should solve which questions
        per_student = total // len(students)
        extra = total % len(students)

        print(f"Each student should solve {str(per_student)}.\n")
        time.sleep(0.9)
        start = 0
        for student in students:
                end = start + per_student
                assigned = questions[start:end]
                start = end

                print(f"{student}'s questions: {', '.join(map(str, assigned))}")
                time.sleep(0.8)

        leftover_questions = questions[start:]
        if extra != 0:
                print(f"\nThere are {str(extra)} leftover questions that couldn't be split fairly among the students.")
                time.sleep(0.8)
                print(f"Leftover questions: question number {', '.join(map(str, leftover_questions))}")



# --- Main program ---

greet()

questions, total = questions()

students = get_students()

extra = identify(students, questions, total)

time.sleep(1)

print("\nAll questions have been assigned. Thank you for using the program! 😊")

