from tabulate import tabulate
number_l=[]
number=0
larg_cha=0

with open('books_and_chapters.txt') as scriptures:
    for names in scriptures:
        div=names.split(':')
        book= div[0].strip()
        chapter= int(div[1])
        script=div[2].strip()
       
        print(f'\nScripture: {script}, Book: {book}, Chapter: {chapter}') 
        number_l.append(chapter)
        if chapter == max(number_l):
            larg_cha= chapter
            larg_book=book
    print(f'\nThe book with the largest number of chapters is {larg_book} with {larg_cha}')    
                

        
        

  