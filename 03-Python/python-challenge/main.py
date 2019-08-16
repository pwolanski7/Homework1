import os
import csv

budget_data = os.path.join('Resource', 'budget_data.csv')
print(budget_data)

with open (budget_data, newline='') as budget_data2:
    csv_reader = csv.reader(budget_data2, delimiter=',')
    print(csv_reader)

    csv_header = next(csv_reader)
    print(f"CSV Header: {csv_header}")
    for rows in csv_reader:
        print(rows)