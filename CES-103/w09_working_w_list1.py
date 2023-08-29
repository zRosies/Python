with open('hr_system.txt') as worker_list:
    for names in worker_list:
        name= 'Name:'
        parts= names.split()
        names= parts[0]
        id= int(parts[1])
        profession=parts[2]
        salary=parts[3]
        salary_mode= float(salary)
        #name_correct= names.strip()
        #print(' ')
        if profession == 'Engineer':
            salary_mode+= 1000 
        
        print(f'{names} (ID: {id}), Title: {profession} - ${salary_mode:.2f}')
