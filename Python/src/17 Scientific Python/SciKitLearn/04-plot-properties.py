from sklearn.datasets import load_iris

# load iris data set
iris = load_iris()
X = iris.data
Y = iris.target

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

figure = plt.figure()
ax = figure.add_subplot(1,1,1, projection='3d')


# combine data and target
Z = []
for x, y in zip(X, Y):
    Z.append([*x, y])   #@IGNORE:55

print(Z)
colors = ["red", "green", "blue"]

for sl, sw, pl, pw, r in Z:
    ax.scatter(sl, sw, pw, c=colors[r], marker='o')
    
ax.set_xlabel('sepal length')
ax.set_ylabel('sepal width')
ax.set_zlabel('petal width')

plt.show()

