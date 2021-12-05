# get inputs
with open('input.txt') as f:
    commands = f.readlines()
    f.close()

position = 0
depth = 0

# loop though commands
for command in commands:
    # get movement and value
    movement, amount = command.split(" ")
    # process
    if movement == "forward":
        position = position + int(amount)
    elif movement == "down":
        depth = depth + int(amount)
    elif movement == "up":
        depth = depth - int(amount)
    else:
        print("Unknown command!")

# multiply position by depth
print ("Answer: " + str(position * depth))