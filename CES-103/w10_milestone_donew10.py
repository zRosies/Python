#'Creativity':
# 1-The program displays the NAME and the number when the item is removed. 
# 2- I added a payment action that calculates the change. Also, If the person pays for the items the loop stops.
# 3- Your credit/debit card password is 2351. 
items=[]
prices=[]
selects=['','Please, select one of the following:','','1. Add an item', '2. View chart','3. Remove item', '4. Compute total', '5. Pay','6. Quit']
total=0
user=0
price=0

print('\nWelcome to the Shopping Cart Program')

while user != 6:
    for select in selects:
        
        print(select)
    user=int(input('\nPlease, enter an action: '))
    if user == 1:
            item= input('\nWhat item would you like to add? ')
            item=item.capitalize()
            items.append(item)
            print(f"\n'{item}' has been added to the chart")
            price = float(input(f"\nWhat is the {item}'s price? "))
            prices.append(price)
    if user ==2:
        print('\nThe contents of the shopping cart are: ')
        for i, item in enumerate(items): 
            item=items[i]
            price= prices[i]  
            print(f'{i+1}. {item} ----- ${price:.2f}')  
    if user ==3:
        pop=int(input('\nChoose the number of the item you want to remove: '))
        while pop > len(items) or pop <= 0 :
            pop=int(input('\nSorry, this number is not in the list. Choose the number of an item within the list:'))
        print(f"\nYou have selected the number {pop}. \
                \nThe item '{items[pop -1]}' has been removed from the list!")    
        items.pop(pop-1) #I poped in the final so the name of the item removed can be displayed correctly.
        prices.pop(pop-1)    
    if user == 4: 
        total= sum(prices)
        print('\nThe total price of the items in the shopping cart is ${:.2f}!'.format(total))
    if user== 5: #Creativity \/
        user=input('\nWhat is your payment method(CREDIT CARD, DEBIT CARD, or CASH)? ')
        if user.upper() =='CREDIT CARD' or user.upper()=='DEBIT CARD':
            password=int(input(f'\nInsert your {user.upper()} and PASSWORD:'))
            while password != 2351: #Symbolic:  As I don't have a method to compare if the user's password is correct, I created one so the user can't get out without paying.
                password=int(input('\nPassword incorrect, try again: '))
            print('\nYour payment has been made sucessfully!')
            user=6
        elif user.upper()=='CASH':
            payment=float(input('\nWhat is the payment amount? '))
            total=sum(prices)
            change = payment - total
            while change < 0: #loops if the user pays less than the total.
                payment=float(input('\nPlease, insert a sufficient amount of money: '))
                total=sum(prices)
                change = payment - total
            print(f'\nYour change is ${change:.2f}!')
            user=6        
print('\nThank you, goodbye!')        
