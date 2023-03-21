import functions as F
import leftStory as l

def main():
    F.cls()

    F.animateText('Welcome brave adventurer to the world of [-----]. A great adventure awaits you')

    input('\n\n[Press enter to start the game]\n\n')

    F.cls()

    choicesLoop = True
    while choicesLoop is True:

        F.animateText('You see what looks like a a pathway that splits off two ways. On the left it \nsplits off to what looks like a dark forest and to the right it looks like a \npathway that leads to a nearby village.\n\nWhat do you plan to do? ')

        menuList = ['\n\n----------Choices!----------\n\n', 'Enter the forest on the left', 'go towards the village on the right', 'Leave']

        menuChoice = F.runMenu(menuList)

        if menuChoice == 1:
            F.animateText('You enter the forest!\n')
            l.lStory()
        
        elif menuChoice == 2:
            F.animateText('You find a small village!\n')

        elif menuChoice == 3:
            F.animateText('Goodbye. better luck next time...')
            quit()

if __name__ == '__main__':
    main()
