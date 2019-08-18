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

#open the csv file
with open (budget_data, newline='') as budget_data2:
    
    #assign the reader to a variable
    csv_reader = csv.reader(budget_data2, delimiter=',')
    
    #look for a header in the csv
    if csv.Sniffer().has_header:
        next(csv_reader)

    #loop through to get total months, the net total, create a list of losses, and a list of profits
    for row in csv_reader:
       total_months += 1
       net_total += int(row[1])
       if int(row[1]) < 0:
           losses_total.append(int(row[1]))
       if int(row[1]) > 0:
           profit_total.append(int(row[1]))

    #calculate the average change
    average_change = net_total/total_months

    #print results on the terminal
    print(f'')
    print(f"Financial Analysis")
    print(f'--------------------------------')
    print(f'Total Months: {total_months}')
    print(f'Net Total: ${net_total}')
    print(f'Average Change: ${round(average_change,2)}')
    print('Greatest Increase in Profits: $', max(profit_total))
    print(f'Greatest Decrease in Profits: $', min(losses_total))

#close the csv file
budget_data2.close()

#assign the min and max to variables
mini_loss = min(losses_total)
max_prof = max(profit_total)

#add all objects to a list for writing to csv
lister = [str(total_months), str(net_total), str(round(average_change, 2)), str(max_prof), str(mini_loss)]

#open csv for writing
with open(output_path, 'w', newline='') as csvfile:
    
    #assign the writer to a variable
    csv_writer = csv.writer(csvfile, delimiter=',')
    
    #write the column headers and list to csv file
    csv_writer.writerow(['Total Months','Net Total','Average Change', 'Greatest Profit Increase','Greatest Profit Decrease'])
    csv_writer.writerows([lister])
