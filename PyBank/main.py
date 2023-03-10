# Modules
import os
import csv

# Create lists and variables
month=[]
profitloss=[]
monthlyChanges=[]
month_count=0
total=0


#Set path for the file
budget_data = os.path.join(os.getcwd(),"PyBank","Resources","budget_data.csv")
outputfile = os.path.join(os.getcwd(),"PyBank","Analysis","PyBank.txt")


#Read csv
with open(budget_data) as csvfile:
    csvreader=csv.reader(csvfile, delimiter =',')
    header=next(csvreader)
    for row in csvreader:
        month_count +=1
        total +=int(row[1])
        month.append(row[0])
        profitloss.append(int(row[1]))

# first month ProfitLoss value
firstProfitLoss = int(profitloss[0])

# Create list of monthly changes
for i in range (1, len(profitloss)):
    monthlyChanges.append(int(profitloss[i])- firstProfitLoss)
    firstProfitLoss = int(profitloss[i])
    i +=1
    
AvgChange = sum(monthlyChanges) / len(monthlyChanges)

# Find max incraese and min increase  
MaxIncrease = max(monthlyChanges)
MaxDecrease = min(monthlyChanges)

# Find month index for max increase and max decrease

for i in range(len(monthlyChanges)):
    if monthlyChanges[i] == MaxIncrease:
        maxIndex = (i+1)
    elif monthlyChanges[i] == MaxDecrease:
        minIndex = (i+1)

MaxMonth = month[maxIndex]
MinMonth = month[minIndex]


print("Financial Analysis")
print("-"*50)
print(f"Total Months: {month_count}")
print(f"Total Amount: ${total}")
print(f"Average Change: ${round(AvgChange,2)}")
print(f"Greatest Increase in Profits: {MaxMonth} (${MaxIncrease})")
print(f"Greatest Decrease in Profits: {MinMonth} (${MaxDecrease})")


# Write into PyBank.txt

with  open(outputfile, 'w') as output:
    output.write("Financial Analysis\n")
    output.write("-"*50 + "\n")
    output.write(f"Total Months: {month_count}\n")
    output.write(f"Total: ${total}\n")
    output.write(f"Average Change: ${round(AvgChange,2)}\n")
    output.write(f"Greatest Increase in Profits: {MaxMonth} (${MaxIncrease})\n")
    output.write(f"Greatest Decrease in Profits: {MinMonth} (${MaxDecrease})")
    
 

    
                           
    

    