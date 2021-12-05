# get inputs
with open('input.txt') as f:
    commands = f.readlines()
    f.close()

position = 0
depth = 0
aim = 0

# loop though commands
for command in commands:
    # get movement and value
    movement, amount = command.split(" ")
    # process
    if movement == "down":
        aim += int(amount)
    elif movement == "up":
        aim -= int(amount)
    elif movement == "forward":
        position += int(amount)
        depth += (int(amount) * aim)
    else:
        print("Unknown command!")

# multiply position by depth
print ("Answer: " + str(position * depth))