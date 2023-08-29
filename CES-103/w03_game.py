aa= input('\nYou are walking through a dark forest with your SMARTPHONE on your pocket and find a MATCH and a FLASHLIGHT. Which one do you want to pick up?')
#Match scenario..
if aa.upper() == 'MATCH': 
    bbb=input('\nYou pick up the match and strike it, and for an instant, the forest around you is illuminated.\
    You see a large grizzly bear, and then the match burns out. Do you want to RUN or HIDE behind a tree?')
    if bbb.upper() == 'RUN': 
        ccc= input('\nThe bear runned after you, you stumbled on a rock falling the ground and saw a wood on your left. Do you HIT the bear with the wood or PRETEND you are dead? ')    
        if ccc.upper() == 'HIT':    
                print('\nYou hit the bear on its nose and it got infuriated and bit you until you start bleeding and die!')
        if ccc.upper() == 'PRETEND':
                print('\nThe bear thought you were dead and lost its interest on you! You are alive for now')
        else:print('Please, choose an action')       
    elif bbb.upper() == 'HIDE': 
        ccc= input('\nThe bear tried to find find you but he heard another noise and you have a fraction of time to decise. Do you WALK away calmly or WAIT until it leaves!')
        if ccc.upper()== 'WALK':
            input('\nYou tried to walk away calmly but the bear heard your footsteps and chased you, your body was found dead in morning of a sunny forest!' )
        elif ccc.upper()== 'WAIT':
                print('\nYou are lucky, the bear leaves the forest and the national guard found you')
        else: print('\nPlease, choose an action!')   
    else: print('\nPlease, choose an action!')                   
if aa.upper()== 'FLASHLIGHT':
    ddd=input('\nYou pick up the flashlight and turn it on. You see the pathway lit up in front of you, but you thought you also heard something off to the side.\
Do you want to FOLLOW the path or LOOK in the trees for the thing that made the noise?')
    if ddd.upper() =='FOLLOW':
            input('\nYou followed the noise and saw a great bear right in front of you!. Do you HIT it with the flashlight or CLIMB on a tree?')
            if ddd.upper()=='HIT':
                print('\nYou HIT the bear with the flashlight and it got infuriated knocking you on the ground') 
            elif ddd.upper()=='CLIMB':
                print('\nYou started climbing on a tree but you did know that bears can climb on it easily, the bear bit you and you fell on the ground breaking your ribs!')
            else: print('\nPlease, choose an action')        
    elif ddd.upper()== 'LOOK':
        ccc= input('\nYou turned the light into the bear and it started running after you. Do you THROW your FLASHLIGHT on it and run or ..... you are dead?')
        if ccc.upper() == 'THROW':
            print('\nYou hit the bear right on it face, the animal got terrified and runned away')
    else: print('\nPlease, choose an action!')
else: print('Please, choose an item!')    






#else:print('Please, choose an action')






     


#if ccc.upper() == 'HIT': 
    #print('\nYou hit the bear on its nose and it got infuriated and bit you until you start bleeding and die!')
#elif ccc.upper() == 'PRETEND': 
            #print('\nThe bear smelled you and lost the interest on his prey, you are alive for now!')
#elif ccc.upper() == 'THROW': 
                #print('\nYou hit the bear right on it face, the animal got terrified and runned away')
#else:print('Please, choose an action!')#