def board(ttt):
    print(ttt['tl']+'|'+ttt['tm']+'|'+ttt['tr'])
    print('-+-+-')
    print(ttt['ml']+'|'+ttt['mm']+'|'+ttt['mr'])
    print('-+-+-')
    print(ttt['bl']+'|'+ttt['bm']+'|'+ttt['br'])   #This finction creates the board
    
def straight(ttt,t):
    if(t==ttt['tl']and t==ttt['tm']and t==ttt['tr']):
        return True
    if(t==ttt['ml']and t==ttt['mm']and t==ttt['mr']):
        return True
    if(t==ttt['bl']and t==ttt['bm']and t==ttt['br']):
        return True
    if(t==ttt['tl']and t==ttt['ml']and t==ttt['bl']):
        return True
    if(t==ttt['tm']and t==ttt['mm']and t==ttt['bm']):
        return True
    if(t==ttt['tr']and t==ttt['mr']and t==ttt['br']):
        return True
    return False                                    #This function cecks the straight set

def slant(ttt,t):
    if(t==ttt['tl']and t==ttt['mm']and t==ttt['br']):
        return True
    if(t==ttt['tr']and t==ttt['mm']and t==ttt['bl']):
        return True
    return False                                    #This function checks the slant set
       
def check(ttt,t):
    if(straight(ttt,t)):
        return True
    if(slant(ttt,t)):
        return True
    return False                                   #Winner decided here
def check2(ttt):
    for i in ttt.values():
        if(i==' '):
            return False
    return True                                    #This when called results in a draw

ttt={'tl':' ','tm':' ','tr':' ',
     'ml':' ','mm':' ','mr':' ',
     'bl':' ','bm':' ','br':' '}
print("""Instructions:
A Player can give his move as
tl   |tm    |tr
ml   |mm    |mr
bl   |bm    |br.
P.S. The moves are case sensitive""")
board(ttt)
p1=input("Player 1's name: ")
p2=input("Player 2's name: ")
t1=input("Symbol Player 1 wants(X/O): '")
t2=''
if(t1=='X' or t1=='x'):
    t2='O'
else:
    t2='X'

while( True ):
    x=input(p1+'\'s'+' move: ')
    ttt[x]=t1
    board(ttt)
    if(check(ttt,t1)):
        print(p1+'('+t1+') Wins')
        break
    if(check2(ttt)):
        print('It\'s a Draw')
        break
    y=input(p2+'\'s'+' move: ')
    ttt[y]=t2
    board(ttt)
    if(check(ttt,t2)):
        print(p2+'('+t2+') Wins')
        break
    if(check2(ttt)):
        print('It\'s a Draw')
        break
print('Thanks for Playing\nPress any key to Exit')
y=input()
print(exit)
