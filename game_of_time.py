from Environment import *
import time

env = Environment(10, 10, "Universe", True)
sleepTime = 0.5

#This is a good starting point, because it rarely dies out
env.set_state(5, 5, True)
env.set_state(6, 5, True)
env.set_state(4, 4, True)
env.set_state(5, 4, True)
env.set_state(5, 3, True)

#Make this state environment's initial state
env.update_initial()

#Run the simulation
while True:
    print("NEXT")
    env.print_map()
    env.step()
    time.sleep(sleepTime)