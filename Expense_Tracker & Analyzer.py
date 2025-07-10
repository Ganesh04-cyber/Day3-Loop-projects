expenses=[]
daily_expenses=[800,1000,1800,2000]
total_expenses=0
for money in daily_expenses:
    expenses.append(money)
    total_expenses=sum(expenses)
    average=total_expenses/len(expenses)
high=max(expenses)
low=min(expenses)
print("\n list of Daily expenses")
print("Total expenses=",total_expenses)
print("average_expenses=",average)
print("Highest expense=",high)
print("Lowest expense=",low)
