# Module 3
#   Programming Assignment 4
#     Prob-3.py

# <Grant Parkinson>


def letterGrade(score):
    # your code here
    grade_number = int(input("Enter grade number: "))
    if grade_number == 5:
        grade = "A"
        print("Your grade is:", grade)
    elif grade_number == 4:
        grade = "B"
        print("Your grade is:", grade)
    elif grade_number == 3:
        grade = "C"
        print("Your grade is:", grade)
    elif grade_number == 2:
        grade = "D"
        print("Your grade is:", grade)
    elif 0 <= grade_number < 2:
        grade = "F"
        print("Your grade is:", grade)

    else:
        print("\n\nERROR: Enter a value within the range 0-5")

    return grade


def unitTest():
    # your test code here
    letterGrade(1)


if __name__ == "__main__":
    unitTest()
