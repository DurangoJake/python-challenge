import os
import csv

file =('budget_data.csv')

with open(file) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
   
    x = 0
    month_adder = 0
    y = []
    z = 0 

    next (csvreader)
   
    

    
    for row in csvreader:
        
        

    
    
        
        x = x + int(row[1])
        month_adder = month_adder + 1
        y.append(row[1])
        
    
    print(y)


   
    
    
        

    
   
    
    print ("Total months: ", month_adder)
    print ("Total: $",  x)
    print ("Average Change: $", z)
    print("Greatest Increase in Profits: ")
    print("Greatest Decrease in Profits: ")
    

        
       

  



   


    