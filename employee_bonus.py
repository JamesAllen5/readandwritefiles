import csv

employees = open("EmployeePay.csv", "r")

employee_file = csv.reader(employees, delimiter=",")

next(employee_file)

for record in employee_file:
    print("First Name: ", record[1])
    print("Last Name: ", record[2])
    print("Salary: ", record[3])

    salary = float(record[3])
    bonus = float(record[4])
    bonus = salary * bonus
    print("Bonus: ", bonus)
    total_Pay = (salary * bonus) + salary

    print("Total Pay: ", total_Pay)
