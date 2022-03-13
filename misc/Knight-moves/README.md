# Challenge

**Name:** How the knight moves

**Category:** Misc

**Difficulty:** Medium

**Author:** AustinNguyen

**Flag:** ISS{K4n1ght_m0v3_1n_L_Sh4p3}

## Description

Do you know how to move the knight on the chess board?
Try to find the fastest way to capture the flag 

## Solution

There are different searching algorithms that you can try to solve the questions.
One possible solution is to apply breadth-first search.

The ideas of the algorithm:  
1. From the current position, check for all possible squares that the knight can reach
2. Push all unvisited squares into the queue
3. Do the same following process until finding the flag:  
   a. Dequeue the next position  
   b. Check if that position is the destination
   c. If not the destination, do steps 1 and 2.
4. When reaching the final position, backtracking to the start position to get the path the knight travel

The solution code can be found in ./solution
