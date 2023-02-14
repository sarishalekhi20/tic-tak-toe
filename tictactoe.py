def sum(a, b, c ):
    return a + b + c
def draw(xstate, zstate):
    zero='X' if xstate[0] else ('0' if zstate[0] else 0)
    one='X' if xstate[1] else ('0' if zstate[1] else 1)
    two='X' if xstate[2] else ('0' if zstate[2] else 2)
    three='X' if xstate[3] else ('0' if zstate[3] else 3)
    four='X' if xstate[4] else ('0' if zstate[4] else 4)
    five='X' if xstate[5] else ('0' if zstate[5] else 5)
    six='X' if xstate[6] else ('0' if zstate[6] else 6)
    seven='X' if xstate[7] else ('0' if zstate[7] else 7)
    eight='X' if xstate[8] else ('0' if zstate[8] else 8)
    print(f"{zero} | {one} | {two}")
    print(f"--|---|---")
    print(f"{three} | {four} | {five}")
    print(f"--|---|---")
    print(f"{six} | {seven} | {eight}")
def winner(xstate, zstate):
    wins=[[0,1,2] , [3, 4, 5], [6, 7, 8] , [ 0, 3, 6] , [1, 4, 7], [2 , 5 , 8] ,
          [0, 4 , 8] , [2, 4 , 6]]
    for i in wins:
        if(sum(xstate[i[0]], xstate[i[1]], xstate[i[2]])==3):
            print("X won!!!!")
            return 1
        if(sum(zstate[i[0]], zstate[i[1]], zstate[i[2]])==3):
            print("O won!!!!(ngl i was rooting for x)")
            return 0
    return -1
xstate=[0, 0, 0, 0, 0, 0, 0, 0,0]
zstate=[0, 0, 0, 0, 0, 0, 0, 0,0]
turn=1
# 1-> X and 0-> Y
print("Welcome to tic tac toe(prepare to loose haha)")
while(True):
    draw(xstate, zstate)
    if(turn==1):
        print("X's turn ")
        value=int(input("enter a position"))
        # draw(xstate, zstate)
        xstate[value]=1
        # turn=0
    else:
       print("O's turn ")
       value = int(input("enter a position"))
       zstate[value]=1
       # turn=1- turn
    # draw(xstate, zstate)
    #    break
    decider=winner(xstate,zstate)
    if(decider!= -1):
        print("Match Over </3")
        break
    turn = 1 - turn

