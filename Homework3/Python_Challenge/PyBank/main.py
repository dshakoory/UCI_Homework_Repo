#importing the libraries
import os
import csv

#creating the budget object based on the existing csv file
budget = os.path.join("budget_data.csv")
budgetanalysis = os.path.join("budgetanalysis.txt")

#variable definition 
date = []
profandloss = [] 
change = 0
monthscount = 0 #Total number of months
pl = 0 #profit/loss
months = 0


#open the CSV file through the defilned path erlier
with open(budget, newline = "") as csvfile:
    x = csv.reader(csvfile, delimiter = ",")
#headerrow
    y= next(x)

    #Reading the first row
    y = next(x) #y represents the first row of data
    monthscount=monthscount + 1
    pl =pl + int(y[1])
    months = int(y[1])
    
    #Forloop to go through each row
    # i represents the rows
    for i in x:
        
        date.append(i[0])
        
        # Calculate the change, then add it to list of changes
        change = int(i[1])-months
        profandloss .append(change)
        months = int(i[1])
        
        #The total number of months included in the dataset
        monthscount=monthscount + 1

        #The net total amount of "Profit and/or Losses"
        pl = pl + int(i[1])



#Average change in "Profit/Losses between months over entire period"
    Average = sum(profandloss)/(monthscount-1)

    #The greatest increase in profits (date and amount) over the entire period
    gi = max(profandloss ) #gi=greatest Increase in profit
    bindex = profandloss.index(gi) 
    bd = date[bindex] # bd=Best date related to greatest increase

   #The greatest decrease in losses (date and amount) over the entire period
    gd = min(profandloss ) #gd=Greatest Decrease in profit
    windex = profandloss.index(gd)
    wd = date[windex]#greatest decrease in profit date


Resutls=( "Financial Analysis\n"
"---------------------------------------\n"
f"Total Months: {str(monthscount)}\n"
f"Total: ${str(pl)}\n"
f"Average Change: ${str(round(Average,2))}\n"
f"Greatest Increase in Profits: {bd} (${str(gi)})\n"
f"Greatest Decrease in Profits: {wd} (${str(gd)})\n")
print(Resutls)


#your final script should both print the analysis to the terminal and export a text file with the results
with open(budgetanalysis, "w") as txt_file:
    txt_file.write(Resutls)