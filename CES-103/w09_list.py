
checking=[] 
saving=[]
emergency_f=[]
names=[]

list_all=[]
l_len=len(list_all)
print('Enter the names and balances of bank accounts (type: quit when done)')
user=''
while user.upper() != 'QUIT':
    user=input('\nWhat is the name of this account?')
            
    if user.lower()=='checking':
        balance=float(input('\nWhat is the balance? '))
        checking.append(balance)
        list_all.append(balance)
        names.append(user)
        
    elif user.lower()=='savings':
        balance1=float(input('\nWhat is the balance? '))
        saving.append(balance1)
        list_all.append(balance1)
        names.append(user)
    elif user.lower()=='emergency fund':
        balance2=float(input('\nWhat is the balance?'))
        emergency_f.append(balance2)
        list_all.append(balance2)
        names.append(user)
    sum_c= sum(checking)
    sum_b= sum(saving)
    sum_a= sum(emergency_f)

    total= sum_c + sum_b + sum_a


print(list_all,names)
print(saving)
for i, account  in enumerate(list_all):

    if balance in (checking):
        price = list_all[i]
        account= names[i]
    elif balance1 in (saving):
        price=list_all[i]
        account= names[i]
    
    elif balance2 in (emergency_f):
        price= list_all[i]
        account= names[i]

    print(f'{i+1}. {account} -- {price}')
print(f'Total: {total}')  
print(f'Average: {total/len(names)}')

user2=''

while user2.upper() != 'NO':
    user2=input('Do you want to update an account?(YES/NO)')
    index=int(input('What account index do you want to update?'))
    amount=float(input('What is the new amount?'))
    index -=1
    user2='NO'
list_all[index]= amount

for i, account  in enumerate(list_all):

    if balance in (checking):
        price = list_all[i]
        account= names[i]
    elif balance1 in (saving):
        price=list_all[i]
        account= names[i]
    
    elif balance2 in (emergency_f):
        price= list_all[i]
        account= names[i]

    print(f'{i+1}. {account} -- {price}')
print(f'Total: {total}')  
print(f'Average: {total/len(names)}')



#aa=sum(checking) + sum(saving) + sum(emergency_f)
#bb= len(checking)+ len(saving) + len(emergency_f)
#print(f'\nTotal: ${aa:.2f}')
#print(f'Average: ${aa/bb:.2f}')


