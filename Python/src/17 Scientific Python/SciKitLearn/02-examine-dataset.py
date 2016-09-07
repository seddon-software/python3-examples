from sklearn.datasets import load_iris

# load iris data set
iris = load_iris()

# print feature matrix
print(iris.data)

# display feature names
print(iris.feature_names)

# print response vector
print(iris.target)

# print response names
print(iris.target_names)

# print the shapes of X and y
print("shape of feature matrix: {}".format(iris.data.shape))
print("shape of response matrix: {}".format(iris.target.shape))
