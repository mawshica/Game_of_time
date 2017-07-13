from Environment import *
import time

env = Environment(10, 10, "Universe", True)
sleepTime = 0.5

#This is a good starting point, because it rarely dies out
env.setState(5, 5, True)
env.setState(6, 5, True)
env.setState(4, 4, True)
env.setState(5, 4, True)
env.setState(5, 3, True)

#Make this state environment's initial state
env.updateInitial()

#Run the simulation
while(True):
    print("NEXT")
    env.printMap()
    env.step()
    time.sleep(sleepTime)