bank_l=[]
price_l=[]

print('Enter the names and balances of bank accounts (type: quit when done)')
user=''
while user.upper() != 'QUIT':
    user=input('\nWhat is the name of this account?')
    if user.upper() !='QUIT':
        balance=float(input('\nWhat is the balance? '))
        price_l.append(balance)
        bank_l.append(user)
print('\nAcount information:')
max= max(price_l)
for index in range(len(price_l)):
    aa= price_l[index]
    bb= bank_l[index]

    
    print(f'{index}. {bb} -- {aa}')
 
total= sum(price_l)
average= total/len(bank_l)
print(f'\nTotal: ${total:.2f}')
print(f'Average: ${average:.2f} ')


for index in range(len(price_l)):
    aa= price_l[index]
    bb= bank_l[index]
    if price_l[index]== max:
        cc=bank_l[index] #Strech 01.

        
print(f'The highest is: {cc} -- {max}')

user5=(input('\nDo you want to update an acount?'))
while user5.lower() != 'no': #Strech 02.
    user1=int(input('\nWhat acount index do you wan to update?'))
    user2=float(input('What is the new amount?'))
    user5=(input('\nDo you want to update an acount?'))
    price_l[user1]=user2

    for index in range(len(price_l)):
        aa= price_l[index]
        bb= bank_l[index]
        if aa== max:
            cc= bb
        print(f'{index}. {bb} -- {aa}') #Strech 03.




