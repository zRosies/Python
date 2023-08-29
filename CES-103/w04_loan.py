from operator import truediv


Loan= int(input('\nHow large is the loan?'))
Chistory= int(input('\nHow good is your credit history?'))
Income= int(input('\nHow high is your income?'))
Payment= int(input('\nHow large is your down payment?'))



if Loan >= 5:
    if Chistory >=7 and Income >= 7:
        aa = True
    elif Chistory >=7 or Income >=7:
        if Payment >=5:
            aa=True 
        else: aa= False
    else: aa=False

if Loan < 5:
    if Chistory < 4:
        aa= False
    elif Income>=7 or Payment >=7:
        aa= True
    elif Income >=4 and Payment >=4:
        aa= True
    else: aa= False
               


if aa:
    print('Yes')
else: print('No')    

