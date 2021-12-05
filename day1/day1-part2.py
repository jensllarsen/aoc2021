
with open('input.txt') as f:
    measures = f.readlines()
    f.close()

previous_sum = 9999999 # hack to make sure the first measure isn't counted
larger_sums = 0
index = 0

while( index < len(measures) - 3):
    first = int(measures[index])
    second = int(measures[index+1])
    third = int(measures[index+2])

    this_sum = first + second + third
    print("This sum: " + str(this_sum))
    print("Previous sum: " + str(previous_sum))

    if this_sum > previous_sum:
        larger_sums = larger_sums + 1
        print("Bigger!")

    previous_sum = this_sum # stash this sum for next iteration
    index = index + 1

print("Number of increases: " + str(larger_sums))