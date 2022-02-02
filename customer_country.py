import csv

customers = open("customers.csv", "r")

outfile = open("customer_country.csv", "w")

customer_file = csv.reader(customers, delimiter=",")

n = 0
for record in customer_file:
    outfile.write(record[1] + ", " + record[2] + ", " + record[3] + "\n")
    n += 1
print("Customer Count:", n)

outfile.close()
