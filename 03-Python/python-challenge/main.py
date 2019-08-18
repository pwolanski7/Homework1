import os
import csv
total_months = 0
net_total = 0
average_change = 0
losses_total = []
profit_total = []
lister = []

budget_data = os.path.join('Resources', 'budget_data.csv')
output_path = os.path.join("Resources", "Output.csv")

with open (budget_data, newline='') as budget_data2:
    csv_reader = csv.reader(budget_data2, delimiter=',')
    if csv.Sniffer().has_header:
        next(csv_reader)

    for row in csv_reader:
       total_months += 1
       net_total += int(row[1])
       if int(row[1]) < 0:
           losses_total.append(int(row[1]))
       if int(row[1]) > 0:
           profit_total.append(int(row[1]))

    average_change = net_total/total_months

    print(f'')
    print(f"Financial Analysis")
    print(f'--------------------------------')
    print(f'Total Months: {total_months}')
    print(f'Net Total: ${net_total}')
    print(f'Average Change: ${round(average_change,2)}')
    print('Greatest Increase in Profits: $', max(profit_total))
    print(f'Greatest Decrease in Profits: $', min(losses_total))

budget_data2.close()
mini_loss = min(losses_total)
max_prof = max(profit_total)
lister = [str(total_months), str(net_total), str(round(average_change, 2)), str(max_prof), str(mini_loss)]

with open(output_path, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile, delimiter=',')
    csv_writer.writerow(['Total Months','Net Total','Average Change', 'Greatest Profit Increase','Greatest Profit Decrease'])
    csv_writer.writerows([lister])
