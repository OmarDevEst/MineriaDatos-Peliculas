import csv

with open('Csvs/AnnualTicketSales.csv', newline='') as File:  
    reader = csv.reader(File)
    for row in reader:
        print(row)

print("Push prueba")
print("pull prueba")