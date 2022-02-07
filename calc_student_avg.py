import csv

students = open("Student_Scores.csv", "r")

outfile = open("student_avg.csv", "w")

student_file = csv.reader(students, delimiter=",")

for record in student_file:
    name = record[0]
    score1 = float(record[1])
    score2 = float(record[2])
    score3 = float(record[3])
    average = round((score1 + score2 + score3) / 3, 2)
    average = str(average)
    outfile.write(record[0] + ", " + average + "\n")

outfile.close()
