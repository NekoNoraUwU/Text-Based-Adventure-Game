import functions as f
def lStory():

    f.cls()

    f.animateText('\nAs you turn the corner you see a castle. when you walk up to the castle you \nsee a broken hole in the wall.')

    leftLoopStory1 = True
    while leftLoopStory1 == True:

        f.animateText('\nWhat do you do? ')

        menuList = ['\n\n----------Choices!----------\n\n', 'Enter the castle through the hole in the wall', 'knock on the door of the caslte ', 'go back to last area']

        menuChoice = f.runMenu(menuList)

        if menuChoice == 1:
            f.animateText('You enter the castle through the hole in the wall!\n')
            firstDungenRoom()

        elif menuChoice == 2:
            f.animateText('You knock on the door of the castle. Shortly after knocking on the door a hidden \nhatch below you opens up and you fall down.')
        
        elif menuChoice == 3:
           f.animateText('You turn back and ')
           leftLoopStory1 = False


def firstDungenRoom():
    DoorKey = False
    CellKey = False
    
    f.animateText('When you enter the castle you see what looks like a wooden door, and some other things around the room. \n\nMaybe interacting with them will help you find the key')

    firstDungenRoomLoop = True
    while firstDungenRoomLoop == True:

        menuList = ['\n\n----------Choices!----------\n\n', 'the door', 'A worn down painting on the wall', 'A pile of bricks on the floor by the hole in the wall', 'An old desk in the corner of the room', 'A cell for captives']

        menuChoice = f.runMenu(menuList)

        if menuChoice == 1: #The door

            if CellKey == True and DoorKey == False:
                f.animateText("it seems that this key doesn't fit the doors key shape. You may be able to find the \nright key if you keep looking around the room.")
            elif DoorKey == False:
                f.animateText('The door seems to be locked. maybe looking around the room may help you find something \nto unlock the door.')
            elif DoorKey == True:
                f.animateText('The door opens and you press forward')
                firstDungenRoomLoop = False

        if menuChoice == 2: #The painting 
            f.animateText('You take a look at the painting on the wall. It seems to be a painting of the lord of the caslte. \nThere is nothing else to take note of here')

        if menuChoice == 3: #The pile of bricks
            f.animateText('It looks to be a pile of bricks from the hole in the wall. There is nothing to take note of here.')

        if menuChoice == 4: #The desk
            deskLoop = True
            while deskLoop == True:
                menuList = ['\n\n----------Choices!----------\n\n', 'The letter', 'The left draw', 'The right Draw', 'Leave the desk']

                f.animateText('\n\nYou take a look at the desk')

                menuChoice = f.runMenu(menuList)

                if menuChoice == 1: #the letter on the desk
                    f.animateText('It is a letter about [-----]')

                elif menuChoice == 2: #The empty draw
                    f.animateText('You open the draw to see nothing but cobwebs and dust. You decide to close the draw and look elsewhere.')

                elif menuChoice == 3: #The key in the draw
                    f.animateText('You open the draw to see a key by its lonesome. \n\nDo you wish to take the key?')

                    menuList = ['\n\n----------Choices!----------\n\n', 'yes', 'no']
                    menuChoice = f.runMenu(menuList)

                    if menuChoice == 1:
                        f.animateText('You take the key')
                        CellKey = True

                    elif menuChoice == 2:
                        f.animateText('You leave the key and close the draw')

                elif menuChoice == 4:
                    f.animateText('You leave the desk')
                    deskLoop = False

        if menuChoice == 5: #The cell

            if CellKey != True:
                f.animateText('The cell door is locked. maybe looking around might help to find a key to open it.')

            elif CellKey == True:
                cellLoop = True
                while cellLoop == True:

                    f.animateText('\n\nYou enter the cell')

                    menuList = ['\n\n----------Choices!----------\n\n', 'An almost broken skeleton on the floor, chained to a wall', 'A desk in the corner', 'a barred window', 'Leave the cell']
                    menuChoice = f.runMenu(menuList)

                    if menuChoice == 1: #The skeleton
                        f.animateText('While looking at the skeleton on the floor you notice another key in its hand. \n\nDo you wish to take the key?')

                        menuList = ['\n\n----------Choices!----------\n\n', 'yes', 'no']
                        menuChoice = f.runMenu(menuList)

                        if menuChoice == 1:
                            f.animateText('You take the key')
                            DoorKey = True

                        elif menuChoice == 2:
                            f.animateText('You leave the key and look elsewhere')

                    if menuChoice == 2:
                        f.animateText('You walk up to the old desk and all that can be seen on it is the will of the skeleton. \n\n[Put more lore here]')

                    if menuChoice == 3:
                        f.animateText('You look through the window to see the darkened and dying forest. there is nothing to take note of here.')

                    if menuChoice == 4:
                        f.animateText('You leave the cell and go back to the room')
                        cellLoop = False



#find a key to open the door
#old painting which has some cool info, has nothing important
#a pile of bricks, looks like the bricks from the wall
#an old desk in the corner
    #the drawers have a key
    #on the drawer you see an old letter (could be cool lore)
    #an empty draw filled with cobwebs
#a cell (need first key from the draw to unlock)
    #a skeleton with something to open the door in their hand
    #a desk
        #on desk you can see a letter. has skeletons will on it
    #a window which has nothing notable about it other than it letting air into the room