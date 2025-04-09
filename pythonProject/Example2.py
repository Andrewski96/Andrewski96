money = int(input("Enter how many dollars you have: "))
pennies = int(money / 1)
nickels = money / 5
dimes = money / 10
quarters = money /25

print(f'You have {money} which is the same as \n{pennies} pennies\n{nickels} nickels\n{dimes} dimes\n{quarters} quarters')