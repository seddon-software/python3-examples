from sklearn import datasets
iris = datasets.load_iris()
print "iris datase shape =", iris.data.shape
print "iris target shape =", iris.target.shape
print "iris images shape =", iris.images.shape

