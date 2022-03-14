from classes.world import world

wrld = world()

print("Start: ")
wrld.display()


rwd = wrld.attemptMove("right")
print("After Right: ", rwd)
wrld.display()

rwd = wrld.attemptMove("down")
print("After down: ", rwd)
wrld.display()

rwd = wrld.attemptMove("right")
print("After Right: ", rwd)
wrld.display()

rwd = wrld.attemptMove("down")
print("After down: ", rwd)
wrld.display()