
with open('input.txt') as f:
    measures = f.readlines()
    f.close()

previous_measure = 0
larger_measures = 0

for measure in measures:
    this_measure = int(measure)
    print("This measure: " + str(this_measure))
    print("Previous measure: " + str(previous_measure))

    if this_measure > previous_measure:
        larger_measures = larger_measures + 1
        print("Bigger!")

    previous_measure = this_measure # store in previous_measure before starting with the next

print("Number of increases: " + str(larger_measures))