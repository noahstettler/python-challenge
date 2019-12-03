import csv

# Text File
f = open("Bank.txt", "w+")
with open("budget_data.csv") as in_file:
    csv_reader = csv.reader(in_file)
    header = next(csv_reader)
    data = list(csv_reader)
    print("Financial Analysis")

    # Number of Months in the Period
    num_months = len(data)
    str_months = "Total number of months: " + str(num_months)
    print(str_months) 

    # Total Profit\Loss
    total = 0
    for column in data:
      total += int(column[1])
    str_total = "Total Proft or Loss: $" + str(total)
    print(str_total)

    # Average change in revenue 
    changes = []
    months = []
    for i in range(1, len(data)):
      change = int(data[i][1]) - int(data[i - 1][1])
      month = str(data[i][0])
      changes.append(change)
      months.append(month)
    net_change = sum(changes)
    avg_change = round(net_change/num_months,2)
    str_change = "Average Change in Revenue: $" + str(avg_change)
    print(str_change)
    
    # Return the Max increase and decrease along with its month
    max_increase = int(max(changes))
    max_decrease = int(min(changes))    
    month_i = ""
    month_d = ""
    for i, row in enumerate(changes):
      if int(row) == max_increase:
        month_i = months[i]
      if int(row) == max_decrease:
        month_d = months[i]      
    str_increase = "Greatest Increase in Revenue: " + month_i + ", $" + str(max_increase)
    str_decrease = "Greatest Decrease in Revenue: " + month_d + ", $" + str(max_decrease)
    print(str_increase)
    print(str_decrease)
     
f.close()
  
