number_l=[]
number=0
larg_book=0
new_l=[]

user=input('Which volume of scripture would you like to learn more about?')

with open('books_and_chapters.txt') as scriptures:
    for names in scriptures:
        div=names.split(':')
        book= div[0].strip()
        chapter= int(div[1])
        script=div[2].strip()
        if script == 'Book of Mormon':#STRETCH CHALLENGEI
            number_l.append(chapter)
            print(f'\nScripture: {script}, Book: {book}, Chapter: {chapter}') 
            if chapter == max(number_l):
                larg_vo= chapter 
                larg_book= book
                lm=script
        if user.lower() == script.lower(): #strechiii
            new_l.append(chapter)
            if chapter== max(new_l):
                new_larg= chapter
                new_book= book
                new_scri=script
    print(f'\nThe book with the largest number of chapters in the {lm} is {larg_book} with {larg_vo} chapters') #Stretch II
    print(f'\nThe book with the largest number of chapters in the {new_scri} is {new_book} with {new_larg} chapters')  #Stretch III
                