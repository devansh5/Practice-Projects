#Simple tic-tac-toe game 
#for the programmer reference 
# Used two dictionaries for refrencing the user to enter the keypad specified as their postion
#Used Functions and Loops ,Exception Haldling
theboard={'top-L':' ','top-M':' ','top-R':' ',
          'mid-L':' ','mid-M':' ','mid-R':' ',
          'low-L':' ','low-M':' ','low-R':' '}

board_keys={7:'top-L',8:'top-M',9:'top-R',
            4:'mid-L',5:'mid-M',6:'mid-R',
            1:'low-L',2:'low-M',3:'low-R'}
print('You can enter these keys on the specified position associated with it')




print('\n')

print(board_keys)
print('\n')

def printboard(board):
    print(' '+board['top-L']+' '+'|'+' '+board['top-M']+' '+'|'+' '+board['top-R']+' ')
    print('-----------')
    print(' '+board['mid-L']+' '+'|'+' '+board['mid-M']+' '+'|'+' '+board['mid-R']+' ')
    print('-----------')
    print(' '+board['low-L']+' '+'|'+' '+board['low-M']+' '+'|'+' '+board['low-R']+' ')

def restart():
    for i in theboard:
        theboard[i]=' '


def game():
    restart()
    turn='X'
    count=0
    for i in range(9):
        printboard(theboard)
        while True:
            try:
                n=int(input('Turn for'+' '+turn+' '+'enter the position you want to enter: '))
                if n>10:
                    raise KeyError
                break
            except KeyError:
                print("Please type value between 1 to 9")

        if theboard[board_keys[n]] == ' ':
            theboard[board_keys[n]]=turn
            count+=1
        else:
            print("This position is already occupied")
            continue
        
        if count>=5:
            if theboard['top-L']==theboard['top-M']==theboard['top-R']!=' ':
                printboard(theboard)
                print("----"+turn+" "+"won the game"+"----")
                break
            elif theboard['mid-L']==theboard['mid-M']==theboard['mid-R']!=' ':
                printboard(theboard)
                print("----"+turn+" "+"won the game"+"----")
                break
            elif theboard['low-L']==theboard['low-M']==theboard['low-R']!=' ':
                printboard(theboard)
                print("----"+turn+" "+"won the game"+"----")
                break
            elif theboard['low-L']==theboard['mid-M']==theboard['top-R']!=' ':
                printboard(theboard)
                print("----"+turn+" "+"won the game"+"----")
                break
            elif theboard['top-L']==theboard['mid-M']==theboard['low-R']!=' ':
                printboard(theboard)
                print("----"+turn+" "+"won the game"+"----")
                break
            elif theboard['top-L']==theboard['mid-L']==theboard['low-L']!=' ':
                printboard(theboard)
                print("----"+turn+" "+"won the game"+"----")
                break
            elif theboard['top-R']==theboard['mid-R']==theboard['low-R']!=' ':
                printboard(theboard)
                print("----"+turn+" "+"won the game"+"----")
                break
            elif theboard['top-M']==theboard['mid-M']==theboard['low-M']!=' ':
                printboard(theboard)
                print("----"+turn+" "+"won the game"+"----")
                break
        if count==9:
            print("Match is Draw")

        if turn == 'X':
            turn ='O'
        else:
            turn='X'
    rematch=input("If you want to play again ..... Enter Y or N :")
        
    if rematch=="Y":
        game()
    else:
        print("Thankyou for playing the game")
        return 


game()

            

            
            
        



