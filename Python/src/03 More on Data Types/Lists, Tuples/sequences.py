############################################################
#
#    sequences
#
############################################################

# set up a sequence
sequence1 = 2, 3, 5, 7, 11, 13, 17

# iterate through the sequence
for index, value in enumerate(sequence1):
    print index, value

sequence2 = 'A', 'B', 'C', 'D', 'E', 'F', 'G'

# iterate through two sequences at once
for value1, value2 in zip(sequence1, sequence2):
    print value1, value2


sequence3 = 66, 24, 17, 25, 51, 98, 78
for value in reversed(sequence3):
    print value,
print

for value in sorted(sequence3):
    print value,
print


1
