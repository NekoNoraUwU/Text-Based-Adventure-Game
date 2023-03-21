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
            print('\n\nEnter a number from the choices provided...\n')
            print('[Press Enter To Continue]')
      
        except ValueError:
            print('\n\nEnter a whole number from the choices provided...\n')
            print('[Press Enter To Continue]')

        except:
            print('\n\nan unknown error has occured... please try again...\n')
            print('[Press Enter To Continue]')

        else:
            loop = False
            cls()
            return menuChoice

def animateText(text):
    for char in text:
        if char == ('.'):
            print (char, end='')
            sleep(.4)
        else:
            print(char,end='')
            sleep(.05)

def cls():
    for x in range(40):
        print()