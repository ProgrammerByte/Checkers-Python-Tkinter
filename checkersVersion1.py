from tkinter import *

"""Todo: Make checkers images instead of characters, add a win condition, add some extra ui to make it look nicer (maybe prompt players to input their names)"""

"""Make it more like traditional checkers by forcing a piece to jump if it's available"""

def buildgrid():
    #Puts it into a frame however doesnt work yet
    gridframe = Frame(root, width = 10, height = 10)
    grid = list()
    for i in range(8):
        grid.append([])
        for x in range(8):
            
            temp = i + x
            textcolour = "None"
            
            if temp % 2 == 0:
                colour = "White"
            else:
                colour = "Black"

            if i < 3 and colour == "Black":
                textcolour = "Yellow"

            if i > 4 and colour == "Black":
                textcolour = "Red"
                
                
            grid[i].append("")
            grid[i][x] = Button(gridframe, text = "", width = 3, height = 1, bg = colour, font = "Calibri 30 bold", command = lambda i=i, x=x: onclick(grid, i, x))
            if textcolour != "None":
                grid[i][x].configure(text = "O", fg = textcolour)
                
            grid[i][x].grid(row = i, column = x, sticky = "nsew")

    gridframe.grid()

def cleargrid(grid):
    for a in range(len(grid)):
            for b in range(len(grid[a])):
                if grid[a][b]["bg"] == "Pink":
                    grid[a][b].config(bg = "Black")

def moving(grid, i, x, playerdistance, playerlist, player, further, king, movelist):
    repeat = 1

    if king == "Y":
        repeat = 2

    playertemp = player
    for a in range(repeat):
        if king == "Y":
            player = a

        for b in range(2):

            if i + movelist[player] < 8 and i + movelist[player] >= 0 and x + movelist[b] >= 0 and x + movelist[b] < 8:
                
                if grid[i + movelist[player]][x + movelist[b]]["text"] == "":
                    grid[i + movelist[player]][x + movelist[b]].config(bg = "Pink")

                elif grid[i + int(movelist[player])][x + movelist[b]]["fg"] != playerlist[playertemp]:
                    stopped = "N"
                    looped = 1
                    
                    while stopped == "N":
                        idistance = movelist[player] * looped
                        xdistance = movelist[b] * looped
                        idistance = idistance + i
                        xdistance = xdistance + x
                        
                        if idistance + movelist[player] < 8 and xdistance + movelist[b] < 8 and idistance + movelist[player] >= 0 and xdistance + movelist[b] >= 0:
                            if grid[idistance][xdistance]["text"] != "" and grid[idistance][xdistance]["fg"] != playerlist[player] and grid[idistance + movelist[player]][xdistance + movelist[b]]["text"] == "":
                                grid[idistance + movelist[player]][xdistance + movelist[b]].config(bg = "Pink")

                                target[b].append([idistance, xdistance])
                                targetdirection[b].append([idistance + movelist[player], xdistance + movelist[b]])
                            else:
                                stopped = "Y"
                        else:
                            stopped = "Y"
                        looped = looped + 2

def onclick(grid, i, x):
    if "turn" not in globals():
        global turn
        turn = 1

    if "target" not in globals():
        global target
        target = [[],[]]

    if "targetdirection" not in globals():
        global targetdirection
        targetdirection = [[],[]]

    if "king" not in globals():
        global king
        king = "N"
        
    playerlist = ["Yellow", "Red"]
    movelist = [1, -1]
    player = turn % 2
    playerdistance = movelist[player]

    further = playerdistance * 2
    
    global piecetomovei
    global piecetomovex
    #-------------------SELECTING PIECE TO MOVE------------------------------
    if grid[i][x]["bg"] != "Pink":
        cleargrid(grid)
        target = [[],[]]
        targetdirection = [[],[]]

        if grid[i][x]["text"] == "O" and grid[i][x]["fg"] == playerlist[player]:
            king = "N"
            
            moving(grid, i, x, playerdistance, playerlist, player, further, king, movelist)

            piecetomovei = i
            piecetomovex = x



    #---------------------MOVING PIECE--------------------------------------
        elif grid[i][x]["text"] == "X" and grid[i][x]["fg"] == playerlist[player]:
            king = "Y"
            moving(grid, i, x, playerdistance, playerlist, player, further, king, movelist)

            piecetomovei = i
            piecetomovex = x


    else:
        grid[piecetomovei][piecetomovex].configure(text = "", fg = "Black")
        if king == "N":
            grid[i][x].configure(fg = playerlist[player], text = "O")
        else:
            grid[i][x].configure(fg = playerlist[player], text = "X")
       
        for b in range(2):
            if len(targetdirection[b]) > 0:
                for z in range(len(targetdirection[b])):
                    if i == targetdirection[b][z][0]:
                        if x == targetdirection[b][z][1]:
                            for h in range(z + 1):
                                grid[int(target[b][h][0])][int(target[b][h][1])].configure(text = "", fg = "Black")
                            
        targetdirection = list()
        target = list()
        
        cleargrid(grid)
        turn = turn + 1
        

        #--------------------------------Checks if piece is at the end of the board to allow it to move in all directions---------
        if (playerlist[player] == "Red" and i == 0) or playerlist[player] == "Yellow" and i == 7:
            grid[i][x].configure(text = "X")
            

root = Tk()
root.title("Checkers")
root.grid()


buildgrid()
root.mainloop()
