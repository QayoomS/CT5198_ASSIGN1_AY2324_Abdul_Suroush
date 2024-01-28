#Name: Abdul Qayoom Suroush ID: 23201600

NumCustomers = [] # I created an empty list that will be used for collecting number of customer per day.
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
#Created another list which contians days of week. This way for each loop, a different day will be picked.

for day in range (0,7):
    NumCustomer = int(input(f"Enter the number of customer for {days_of_week[day]}: "))
    NumCustomers.append(NumCustomer)
#for the loop, i want my loop goes from 0 [Mondya] to 7 [Sunday] before printing anything.
#with input we get users number for the day and change to intiger (just in case there are not).
#Then, we will add them to NumCustomer list.
Max_Customer = max(NumCustomers)
Min_Customer = min(NumCustomers)
AVg_Customer = sum(NumCustomers)/len(NumCustomers)

#above, we created functions based on the assigment requirement.
# We can use average of other library, but since it is not mentioned we just do simple math to find the average.

print(f"Maximum customer of this week: {Max_Customer}")
print(f"Minimum customer of this week: {Min_Customer}")
print(f"Average customer of this week: {AVg_Customer: .2f}")

#finally, we print them all. To avoid having tens of dismal for the average, i limited it to two by using .2f