
while True:
    amount = input("Please enter a number: ")
    if amount.isdigit():
        break
    else:
        print("You made a mistake. Please enter a valid number.")

while int(amount) > 9:
    k = 0
    for i in range(len(amount)):
        k += int(amount[i])
    amount = str(k)

print(amount)