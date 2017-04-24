############################################################
#
#    simple plot
#
############################################################


import matplotlib.pyplot as plt

redCircles = "ro"
plt.plot([1,2,3,4], [1,4,9,16], redCircles)
plt.axis([0, 6, 0, 20])
plt.ylabel("squares")
plt.show()

1