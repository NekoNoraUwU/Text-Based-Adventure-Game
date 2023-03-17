from time import sleep

class ValueOutOfRange(Exception):
    pass

def runMenu(menuList):
    loop = True
    while loop == True:
        try:
            print(menuList[0])
  
            for x in range(1, len(menuList)):
                print(str(x) + ': ' + menuList[x])
  
            menuChoice = int(input('\nPlease make a selection from the list provided: \n'))
            if menuChoice > len(menuList) -1 or menuChoice < 1:
                raise ValueOutOfRange
        except ValueOutOfRange:
            print('\n\nEnter a number from the list provided...\n')
            print('[Press Enter To Continue]')
      
        except ValueError:
            print('\n\nEnter a whole number from the list provided...\n')
            print('[Press Enter To Continue]')

        except:
            print('\n\nan unknown error has occured... please try again...\n')
            print('[Press Enter To Continue]')

        else:
            loop = False
            return menuChoice

def animatedText(TTBA):
    for char in TTBA:
        print(char,end="")
        sleep(.05)
    return TTBA

TTBA = '''The magical world of Naligrad awaits! Join brave warrior Yfon on a thrilling journey full 
of danger, mystery, and excitement. Explore exotic lands, battle fierce monsters, 
and uncover ancient secrets. Along the way, Yfon will discover powerful magic 
spells and artifacts, gain allies, and uncover the sinister plots of the evil 
forces that threaten the land. Join Yfon on the greatest journey of their life - 
an epic fantasy adventure!'''

animatedText(TTBA)

input('\n\n[Press enter to continue]\n\n')

TTBA = 'Brave adventurer, you see a dirt path that splits off to the left or to the right.\n what do you plan to do? '

animatedText(TTBA)

menuList = ['\n\n----------Choices!----------\n\n', 'take the left path', 'take the right path']

menuChoice = runMenu(menuList)

