def new_cap_reg(name):
        
        return name
def new_cap_low(name):
        name= name.lower()   
        return name
def new_cap_upper(name):
        name=name.upper()
        return name

user=input('\nWhat is your message?')

name_lower=new_cap_low(user)
name_upper= new_cap_upper(user)
name_reg= new_cap_reg(user)

for names in (name_upper,name_lower,name_reg):
        print(names)
