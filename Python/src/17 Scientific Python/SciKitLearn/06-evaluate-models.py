from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.datasets import load_iris

# load iris data set
iris = load_iris()
X = iris.data
Y = iris.target


def predict(estimator, message):
    # train
    estimator.fit(X, Y)
    # predict
    prediction = estimator.predict(X)
    # compare with actual
    print(message, metrics.accuracy_score(Y, prediction))

# predict with differnt estimators and parameters
predict(KNeighborsClassifier(n_neighbors=1), "KNeighbors(K=1):")
predict(KNeighborsClassifier(n_neighbors=3), "KNeighbors(K=3):")
predict(KNeighborsClassifier(n_neighbors=5), "KNeighbors(K=5):")
predict(LogisticRegression(), "LogisticRegression(defaults):")
