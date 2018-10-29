# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 16:53:25 2018

Solves Ghyston Grid Puzzle

@author: Joey Green
"""

tb = [[3,'R','H','S',2,'E','J','I','G',6],
      ['A','L','E','E','Q','P','L','M',6,'H'],
      [2,'J',8,'E','V','I','G',7,'N','T'],
      ['Y',1,'Q','I','Q','W','W',2,'U','Y'],
      [7,'E','Y','B',3,4,'V','Q','S','T'],
      ['A','W','D','S','C','U',5,'R','U','N'],
      ['B',9,'V','R','J','Y','L','W','P',3],
      ['O','N','J',5,'G','L',7,'D','I','H'],
      ['J','X',5,2,'C','N','Z','G',4,'I'],
      ['R','P','Z','G',3,'E','N','S','M',1]]

''' Move through the grid '''
def move(curpos, steps, direc):
    return ((curpos[0] + ((direc==0) * steps) - ((direc==2) * steps)) % 10, (curpos[1] + ((direc==1) * steps) - ((direc==3) * steps)) % 10)

''' Solves grid puzzle given starting position '''
def search(pos, direc=0, i_max=9):
    out = ''
    for i in range(i_max):
        cur = tb[pos[1]][pos[0]]
        if type(cur) is int:
            pos = move(pos, cur, direc)
        else:
            out += cur
            pos = move(pos, pos[0] + pos[1], direc)
        direc = (direc + 1) % 4 # 0, 1, 2, 3 -> right, down, left, up
    return out
    
if __name__ == '__main__':
    
    pos = (0,0)
    direc = 0 
    i_max = 9
    
    for x in range(10):
        for y in range(10):
            print '({},{}): {}'.format(x,y,search((x,y), direc, i_max)) # nothing else hidden :(
