
NumCustomers = []

for day in range (1, 8):
    daily_input = int(input("Enter the Number of customer for today: "))
    NumCustomer = daily_input
    NumCustomers.append(NumCustomer)

Max_Customer = max(NumCustomers)
Min_Customer = min(NumCustomers)
AVg_Customer = sum(NumCustomers)/len(NumCustomers)

print(f"Maximum customer of this week: {Max_Customer}")
print(f"Minimum customer of this week: {Min_Customer}")
print(f"Average customer of this week: {AVg_Customer: .2f}")