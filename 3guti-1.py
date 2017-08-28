# -*- coding: utf-8 -*-
"""
Spyder Editor

Author: Shamrat Akbar 25/07/2017

This is a temporary script file.
"""
import sys

sys.setrecursionlimit(1500)

print(sys.getrecursionlimit())

get_win_state=False
win_pos=-2

_win = False


board = {"0":[1,3,4],"1":[0,2,4],"2":[1,4,5],"3":[0,4,6],"4":[0,1,2,3,5,6,7,8],"5":[2,4,8],"6":[3,4,7],"7":[4,6,8],"8":[4,5,7]}

plyboard = [-1,-1,-1,0,0,0,1,1,1]

def win(player,w_pos):
    win_state = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    global win_pos
    
    start_range=-1
    end_range=-1
    if player==-1:
        start_range=0
    else:
        end_range=2
    if w_pos==-2:
        return -2
    
    for i in range(0,len(win_state)):
        #print(str(plyboard[win_state[i][0]])+" "+str(plyboard[win_state[i][1]])+" "+str(plyboard[win_state[i][2]]))
        if (start_range !=i and end_range!=i and plyboard[win_state[i][0]] != 0 and plyboard[win_state[i][0]] == plyboard[win_state[i][1]] and plyboard[win_state[i][1]] ==plyboard[win_state[i][2]]):
            
#            print("w_pos :"+str(w_pos))
#            print("win Pos: "+str(win_pos))
           
            if w_pos > win_pos:    
                win_pos=w_pos
            return plyboard[win_state[i][2]]
    return -2        

def minimax(player,w_pos):
    winner = win(player, w_pos)
    if winner!=-2:
        print("get winning state")
        return int(winner)*int(player)
    move=-1
    score=-2
    
    new_pos = []

        
        
    for i in range(0,len(plyboard)):
        if plyboard[i]==player:
            new_pos.append(i)
            #print(index_start)
       
            
    for i in new_pos:
         m = board[''+str(i)+'']

         for j in m:
            if move != -1:
                break
            if plyboard[j]==0:
                plyboard[i]=0
                plyboard[j]=player
                
                
                #print("win_pos: "+str(win_pos)+" old_pos: "+str(i))    
                new_p_val = -1*player
                thisScore =  -minimax(new_p_val,j)
#                print("Player: "+str(player)+" is on "+str(i)+" position and can move on:"+str(j))
#                print("-------------")
#                print(str(plyboard[0])+" | "+str(plyboard[1])+" |"+str(plyboard[2]))
#                print("--+---+--")
#                print(str(plyboard[3])+" | "+str(plyboard[4])+" |"+str(plyboard[5]))
#                print("--+---+--")
#                print(str(plyboard[6])+" | "+str(plyboard[7])+" |"+str(plyboard[8]))
#                print("-------------")
                if thisScore > score:
                    score=thisScore
                    move = j
                   
                        
                plyboard[i]=player
                plyboard[j]=0
                
                    
    if move==-1:  
        return 0
    return score                  
         
                    
        
def compmove(mv):
    global win_pos
    global _win
    move=-1
    oldPos = -1
    score=-2
    
    new_pos = []
    for i in range(0,len(plyboard)):
        if plyboard[i]==1:
            new_pos.append(i)
    is_win=0         
    for i in new_pos:
        m = board[''+str(i)+'']
         
        for j in m:
            if plyboard[j]==0:
                plyboard[i]=0
                plyboard[j]=1 
                is_win = win(1,j)
                if is_win != -2:
                    break
                plyboard[i]=1
                plyboard[j]=0     
        if is_win != -2:
            break
    if is_win != -2:
        print("PC Win The Game")
        _win = True
        return            
            
    for i in new_pos:
         m = board[''+str(i)+'']
         for j in m:
            if plyboard[j]==0:
                plyboard[i]=0
                plyboard[j]=1
                thisScore =  -minimax(-1,-2)
                plyboard[i]=1
                plyboard[j]=0
                if thisScore > score:
                    score=thisScore
                    move = j
                    oldPos = i
#                    print(str(i)+" can move on:"+str(j))
    print("win_pos: "+str(win_pos)+" old_pos: "+str(oldPos))            
    if win_pos == oldPos:
        new_pos.remove(win_pos)
        one_move = False
        win_pos=-2
        for i in new_pos:
            m = board[''+str(i)+'']
            for j in m:
                
                if plyboard[j]==0:
                    one_move=True
                    plyboard[i]=0
                    plyboard[j]=1
                    break
            if one_move:
                break                
                
    else:                      
        plyboard[oldPos]=0
        plyboard[move]=1
    
def playermove(mv):
    opos=mv.split("->")[0]
    npos=mv.split("->")[1]
    plyboard[int(opos)]=0
    plyboard[int(npos)]=-1
#    print(str(plyboard[0])+" | "+str(plyboard[1])+" |"+str(plyboard[2]))
#    print("--+---+--")
#    print(str(plyboard[3])+" | "+str(plyboard[4])+" |"+str(plyboard[5]))
#    print("--+---+--")
#    print(str(plyboard[6])+" | "+str(plyboard[7])+" |"+str(plyboard[8]))
#    print("-------------")
    compmove(mv)
    print(str(plyboard[0])+" | "+str(plyboard[1])+" |"+str(plyboard[2]))
    print("--+---+--")
    print(str(plyboard[3])+" | "+str(plyboard[4])+" |"+str(plyboard[5]))
    print("--+---+--")
    print(str(plyboard[6])+" | "+str(plyboard[7])+" |"+str(plyboard[8]))

var = input("Please enter position: ")
print(var.split("->")[0])
playermove(var)
while _win == False:
    var = input("Please enter position: ")
    win_pos = -2
    playermove(var)

#minimax(-1)

#win(1,5)


