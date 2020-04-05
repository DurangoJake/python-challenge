import os
import csv

file =('budget_data.csv')

output_path =("outputbudget.csv")

with open(file) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
   
    x = 0
    month_adder = 0
    month_list = []
    y = []
    z = 0 

    next (csvreader)

    for row in csvreader:
    
        x = x + int(row[1])
        month_adder = month_adder + 1
        y.append(row[1])
        month_list.append(row[0])


    length = len(y) - 1
    new_list = []
    perchange = 0
    for u in range(length):
        changer = int(y[u+1]) - int(y[u])
        perchange = perchange + changer
        new_list.append(changer)
        
    

    totalchange = perchange / length
  
        
    high = max(new_list)
    low = min(new_list)

    index_high = new_list.index(high) + 1

    index_low = new_list.index(low) + 1

    print ("Financial Analysis")
    print ("-"*60)
    print ("Total months: ", month_adder)
    print ("Total: $",  x)
    print ("Average Change: $", totalchange)
    print("Greatest Increase in Profits: ", month_list[index_high],  "($",high , ")")
    print("Greatest Decrease in Profits: ", month_list[index_low], "($",low , ")" )



with open (output_path, 'w') as csvfile:

    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(['Total months: ','Total: $','Average Change: $', 'Greatest Increase in Profits: ','Greatest Decrease in Profits: ' ])
    csvwriter.writerow([month_adder, x, totalchange, month_list[index_high], month_list[index_low] ])

        
       

  



   


    