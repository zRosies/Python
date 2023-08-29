
child = float(input("\nWhat is the price of a child's meal? "))
adult= float(input("What is the price of an adult's meal? "))
children= int(input("How many children are there? "))
adults= int(input("How many adults are there? "))
sales= float(input("What is the sale tax rate? "))

adulty= adult * adults
childy= child * children
sub= childy + adulty
satx= sub * sales/100
total= sub + satx

print(f"\nSubtotal: ${sub:.2f}")
print(f"Sales tax: ${satx:.2f}")
print(f"Total: ${total:.2f} ")

pay=float(input("\nWhat is the payment amount? "))
change= pay-total

print(f"\nChange: ${change:.2f}")


number=-1

while number <= -1:
    number=float(input('\nPlease, choose a positive number!'))
print('\nThe number is {:.2f}'.format(number))    


