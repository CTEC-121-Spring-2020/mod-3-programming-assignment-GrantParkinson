# Module 3
#   Programming Assignment 4
#     Prob-2.py

# <Grant Parkinson>

'''
Your IPO comment goes here
Input: Name, Wage, hours
Process: Check for overtime hours(if no overtime hours calc gross income), find how many overtime hours,
multiply hourly wage by 1.5 and multiply that wage by overtime hours, add overtime income to base pay wage, calc taxes, calc medical, calc take home pay.
Output: Name, regular wage total, overtime total, total wages, tax withheld, insurance withheld, takehome pay.

'''


def main():
    employee_name = str(input("What is your name?: "))
    employee_wage = eval(input("What is your hourly wage?: "))
    employee_hours = eval(input("How many hours did you work?: "))
    overtime_wage = employee_wage*1.5

    if employee_hours >= 40:
        overtime_hours = employee_hours - 40
        overtime_income = overtime_hours*overtime_wage
        gross_income = employee_wage * \
            (employee_hours - overtime_hours) + overtime_income
    else:
        overtime_hours = 0
        overtime_income = 0
        gross_income = employee_wage*employee_hours

    taxes = gross_income * .2
    medical_insurance = gross_income * .1
    take_home_income = gross_income - taxes - medical_insurance

    print("\nName:", employee_name)
    print("Regular wages:", employee_wage * (employee_hours - overtime_hours))
    print("Overtime wages:", overtime_income)
    print("Total Wages:", gross_income)
    print("Tax withholding:", taxes)
    print("Insurance withholding:", medical_insurance)
    print("Take home pay:", take_home_income)


main()
