aa= input('\nYou are walking through a dark forest with your SMARTPHONE on your pocket and find a MATCH and a FLASHLIGHT. Which one do you want to pick up?')
#Match scenario..
if aa.upper() == 'MATCH': 
    bbb=input('\nYou pick up the match and strike it, and for an instant, the forest around you is illuminated.You see a large grizzly bear, and then the match burns out. Do you want to RUN, HIDE behind a tree?, you MAKE a weapon with the wood?')
    if bbb.upper() == 'RUN': 
        ccc= input('\nThe bear ran after you, you stumbled on a rock falling on the ground, and saw a stick of wood on your left. Do you HIT the bear with the wood, TRY to stand up and run, or PRETEND you are dead? ')    
        if ccc.upper() == 'HIT':    
                print('\nYou hit the bear on its nose and it got infuriated and bit you until you start bleeding and die!')
        elif ccc.upper() == 'PRETEND':
                print('\nThe bear thought you were dead and lost its interest in you! You are alive for now!')
        elif ccc.upper()=='TRY':
            print('\nYou tried to stand up but the bear grabbed your legs, you started bleeding too much and died!')        
        else:print('\nPlease, choose an action')       
    elif bbb.upper() == 'HIDE': 
        ccc= input('\nThe bear tried to find you but he heard another noise and you have a fraction of time to decide. Do you WALK away calmly, WAIT until it leaves!, or THROW a rock on the trees to make noise?')
        if ccc.upper()== 'WALK':
            input('\nYou tried to walk away calmly but the bear heard your footsteps and chased you, your body was found dead in the morning of a sunny forest!' )
        elif ccc.upper()=='THROW':
            print('\nYou got a rock and hit the bushes with it, the bear got distracted by the noise and went away! ')    
        elif ccc.upper()== 'WAIT':
                print('\nYou are lucky, the bear leaves the forest and the national guard found you!')
        else: print('\nPlease, choose an action!')
    elif bbb.upper()=='MAKE':
        ccc=input('\nYou take a stick and used it as a bat to protect yourself. Do you KEEP walking into the forest, GO back home, or HUNT the bear?')
        if ccc.upper()=='KEEP':
            print('\nAs you go into the forest your phone rings, it is your mother calling you home!')
        elif ccc.upper()=='GO':
            print('\nAs you go home, you hear a huge sound coming from behind you, you leave the stick on the ground and run as fast as you can until you get home!')
        elif ccc.upper()=='HUNT':
            print('\nYou follow the noise until you get near the river where you see the bear, you throw a rock at the bear starting a fight near the river. The animal goes towards you knocking you to the ground and biting your legs. You hear a shot from across the river, the animal falls on you! A hunter saved your life!')
        else:print('\nPlease, choose an action!')
        print()
    else: print('\nPlease, choose an action!') 
#Flashlight scenario                      
elif aa.upper()== 'FLASHLIGHT':
    ddd=input('\nYou pick up the flashlight and turn it on. You see the pathway lit up in front of you, but you thought you also heard something off to the side.\
Do you want to FOLLOW the path, ILLUMINATE and go into the path toward the river, or LOOK at the trees to find where the noise comes from?')
    if ddd.upper() =='FOLLOW':
            ccc=input('\nYou followed the noise and saw a great bear right in front of you! Do you HIT it with the flashlight, HIDE in the bush, or CLIMB on a tree?')
            if ccc.upper()=='HIT':
                print('\nYou HIT the bear with the flashlight and it got infuriated and got away!') 
            elif ccc.upper()=='CLIMB':
                print('\nYou started climbing on a tree but you did know that bears can climb on it easily, the bear bit you and you fell on the ground, breaking your ribs!')
            elif ccc.upper()=='HIDE':
                print('\nThe bear heard a noise but found nothing, you saw it disappear among the trees! You are safe!')
            else: print('\nPlease, choose an action!')        
    elif ddd.upper()== 'LOOK':
        ccc= input('\nYou turned on the light, saw a bear and it started running after you. Do you THROW your flashlight on it, RUN from the bear, Go toward the road?!')
        if ccc.upper() == 'THROW':
            print('\nYou hit the bear right on its face, and the animal got terrified and ran away!')
        elif ccc.upper()=='RUN':
            print('\nYou ran as fast as you could but the bear got you and now you are dead!')
        elif ccc.upper()== 'GO':
            print('\nYou ran into the road and almost got hit by a car. Thankfully you are safe!')
        else:print('\nPlease,choose an action!')            
    elif ddd.upper()=='ILLUMINATE' :
        ccc=input('\nYou illuminate the path and walk into the river seeing a hunter on the other side. Do you say HELLO, WAVE at him, or TURN your back at him and keep walking?')      
        if ccc.upper()=='HELLO':
            print('\nThe hunter looks at you and tells you to take care because three people were found dead in that forest this month!')
        elif ccc.upper()=='WAVE':
            print('\nYou waved at the hunter and he waved back at you!')
        elif ccc.upper()=='TURN':
            print('\nYou turned your back to the hunter and heard a huge boom, it was a bullet head in your direction, you look around and sees a dead bear near you! The hunter saved your life!')    
        else:print('\nPlease,choose an action!')
    else: print('\nPlease, choose an action!')
#Smartphone scenario
elif aa.upper()== 'SMARTPHONE':
        ff=input('\nYou unlocked your smartphone and it rang with a message from your friend. Suddenly you hear a roar. Do you UNLOCK your smartphone, WALK into the forest, or ACCEPT the call on your phone? ')
        if ff.upper()=='UNLOCK':
            gg=input('\nAs soon as you unlock your smartphone, you see a huge shadow next to you! Do you RUN, THROW your smartphone on the shadow, or STAY still?')
            if gg.upper()=='RUN':
                print('\nYou run as fast as you can, but the shadow follows you until the river. The moonlight displays a silhouette of a huge bear that runs away when it hears a sound of a shot across the river! You alive thanks to a local hunter!')
            elif gg.upper()=='STAY':
                print('\nAs you remain where you are, the shadow slowly goes away, you turn on your flashlight and sees a bear far from you. You are alive for today!')
            elif gg.upper() == 'THROW':
                print('You throw the smartphone on the shadow turning on the flashlight showing the truly indentity of the shadow, a huge bear that got infuriated and killed you!')   
            else:print('\nPlease, choose an action!')    
        elif ff.upper()=='WALK':
            gg=input('\nAs you walk into the forest you see the shadow following you slowly, the roar is even louder. Do you TURN away and go home, STOP and remain quiet, TRY to touch the shadow?')
            if gg.upper()=='TURN':
                print('\nAs you get near the road, you look back seeing the shadow again, you will never know what it was!')
            elif gg.upper()=='STOP':
                print('\nAs you remained quiet, the shadow roared again. You did not say a word and the shadow disappeared!')
            elif gg.upper()=='TRY':
                print('\nWhen you touched the shadow, you felt the skin of a monster that knocked you to the ground and roared so loud on your face. You woke up in the forest on the next day not knowing what happened!')
            else: print('\nPlease, choose an action!')
        elif ff.upper()=='ACCEPT':
                gg=input('\nAs you accept the call, a huge bear bit your hand, and your cellphone altogether with you falls on the ground. Do you SCREAM for help, PRETEND you are dead, TRY to get your phone and call someone for help? ')
                if gg.upper()=='SCREAM':
                    print('\nYou screamed so loud as the bear bites your legs, no one hears your screams! Your body is found in the forest in the morning!')
                elif gg.upper()=='PRETEND':
                    print('\nThe monster did not stop biting you until it thought you were dead, you lost plenty of blood but could make it until the next day. You were rescued in the morning and taken into a hospital!')    
                elif gg.upper()=='TRY':
                    print('\nYou tried to get your phone but the bear pulled your leg. You kicked the bear, got your phone, and started running toward the road. You were found by a driver and your wounds were treated!')
                else: print('\nPlease, choose an action!')
        else:print('\nPlease, choose an action!')            
else: print('\nPlease, choose an item!')    
# Done!!!:D