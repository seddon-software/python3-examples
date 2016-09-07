from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris

# load iris data set
iris = load_iris()
X = iris.data
Y = iris.target

# two unclassified iris's
iris1 = [3, 5, 4, 2]
iris2 = [5, 4, 3, 2]

def predict(estimator, message):
    # train
    estimator.fit(X, Y)
    # estimate
    print(message, estimator.predict([iris1, iris2]))

# predict with differnt estimators and parameters
predict(KNeighborsClassifier(n_neighbors=1), "KNeighbors(K=1):")
predict(KNeighborsClassifier(n_neighbors=3), "KNeighbors(K=3):")
predict(KNeighborsClassifier(n_neighbors=5), "KNeighbors(K=5):")
predict(LogisticRegression(), "LogisticRegression(defaults):")
