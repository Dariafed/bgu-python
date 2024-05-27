   
while True:
    amount = input("Please enter a number: ")
    if amount.isdigit():
        amount = int(amount)
        break
    else:
        print("You made a mistake. Please enter a valid number.")

for i in range(1, amount + 1):
    print((amount - i) * ' ' + (2 * i - 1) * '*' + (amount - i) * ' ')