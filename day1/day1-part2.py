
with open('input.txt') as f:
    measures = f.readlines()
    f.close()

previous_measure = 9999 # hack to make sure the first measure isn't counted
larger_measures = 0

for measure in measures:

print("Number of increases: " + str(larger_measures))