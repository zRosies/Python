
items_list=[]

user=''
print('Please enter the items of the shopping list (type: QUIT to finish)')
while user.upper() != 'QUIT':
        user=input('item: ')
        if user.upper() !='QUIT':
            items_list.append(user)

print()
for i in range(len(items_list)):
    item= items_list[i]
    print(f'{i}. {item}') 


user3=int(input('\nWhich item would you like to change?'))
user2=input('What is the new item?')

items_list[user3]=user2

for i in range(len(items_list)):
    item= items_list[i]
    print(f'{i}. {item}') 

