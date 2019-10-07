#!/usr/bin/python
# -*- coding: utf8 -*-

#Author Παναγιώτης Πράττης-Panagiotis Prattis Π15120
#This is the 9th exercise from the python exercise series for the class "ΕΙΣΑΓΩΓΗ ΣΤΗΝ ΕΠΙΣΤΗΜΗ ΤΩΝ ΥΠΟΛΟΓΙΣΤΩΝ - COMPUTER SCIENCE INTRODUCTION", University of Pireus
#Project's demands:
# Write code that keeps in memory a table of 10 columns and 20 rows and that
# plays "Tetris" only by adding L randomly in the table. L is an element with a height
# of 3 blocks and 2 width.
# The program ends when the L surpass in height 20 blocks, then it prints how many L
# managed to enter. The program's only output is the number of the L, not the game.

import random

nRows = 20;
nColumns = 10;
# Create table, the empty space will be the zeroes and the L will be the aces
table = [[0 for i in range(nColumns)] for j in range(nRows)];

lWidth = 2;
lHeight = 3;
lCount = 0;

gameover = False;
while not gameover:
    # Position of the L's vertix
    posL = random.randint(0, nColumns-lWidth);
    for i in range(0, nRows):
        goNext = False;
        for j in range(0, lWidth):
            # if no L and not the end of table, continue checking
            if(table[i][posL+j] == 0 and i < nRows-1):
                continue;
            # if end of table and no L yet, continue checking this row's cells
            # to see if we can put the L here
            elif( table[i][posL+j] == 0 and j < lWidth-1 and i == nRows-1 and i-lHeight+1 >= 0):
                continue;
            # If it reached the end of table and there is no L, put it there
            elif( table[i][posL+j] == 0 and j == lWidth-1 and i == nRows-1 and i-lHeight+1 >= 0):
                # draw L on this row
                for k in range(0, lWidth):
                    table[i][posL+k] = 1;
                for v in range(1, lHeight):
                    table[i-v][posL] = 1;
                lCount+=1;
                goNext = True;
                break;
            # If found an L in this row, put the L above it
            elif( table[i][posL+j] == 1 and i-lHeight >= 0 ):
                # draw L on row above
                for k in range(0, lWidth):
                    table[i-1][posL+k] = 1;
                for v in range(1, lHeight):
                    table[i-1-v][posL] = 1;
                lCount+=1;
                goNext = True;
                break;
            # BOOM!
            else:
                gameover = True;
                goNext = True;
                break;
        # If an L was drawn or it is game over, restart the cycle that iterates
        # over the rows
        if(goNext):
            break;

#Not necessary according to the project's demands
for i in range(0, nRows):
    print (table[i])
#All steps till the game over
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in table]))
    print('------------------------------------')

print (lCount, " L's were spawned.")
