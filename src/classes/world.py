from classes.state import state
import numpy as np

class world:
    """The Gridworld 'world'"""
    theWorld = []

    ## (row, column)
    obstacles = [
                    (2,2),
                    (3,2)
                ]
    punish =    [
                    (4,2)
                ]
    start = (0,0)
    goal =  (4,4)

    def __init__(self) -> None:
        # build the world
        self.theWorld = np.empty((5,5),state)
        for i in range(5):
            for j in range(5):
                # check if obstacle 
                if((i,j) in self.obstacles):
                    self.theWorld[i][j] = state(0,False)
                elif((i,j) in self.punish):
                    self.theWorld[i][j] = state(-10,True)
                elif((i,j) == self.goal):
                    self.theWorld[i][j] = state(10,True)
                else:
                    self.theWorld[i][j] = state(0,True)
        self.currentLoc = self.start

    def display(self) -> None:
        # print world to cmd line
        for i in range(len(self.theWorld)):
            for j in range(len(self.theWorld[i])):
                out = "["
                st = self.theWorld[i][j]
                if((i,j) == self.currentLoc):
                    out += "*"
                elif(not st.enterable):
                    out += "█"
                elif(st.enterable and (st.reward == 0)):
                    out += " "
                elif(st.enterable and (st.reward > 0)):
                    out += "+"
                elif(st.enterable and (st.reward < 0)):
                    out += "-"
                out += "]"
                print(out, end='')
            print('') # force newline