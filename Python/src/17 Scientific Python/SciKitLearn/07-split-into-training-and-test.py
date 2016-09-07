from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.cross_validation import train_test_split
from sklearn.datasets import load_iris

# load iris data set
iris = load_iris()
X = iris.data
Y = iris.target


def predict(estimator, message):
    # split data into train and test
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.4, random_state=4)
    # train
    estimator.fit(X_train, Y_train)
    # predict
    prediction = estimator.predict(X_test)
    # compare with actual
    print(message, metrics.accuracy_score(Y_test, prediction))

# predict with differnet estimators and parameters
predict(KNeighborsClassifier(n_neighbors=1), "KNeighbors(K=1):")
predict(KNeighborsClassifier(n_neighbors=3), "KNeighbors(K=3):")
predict(KNeighborsClassifier(n_neighbors=5), "KNeighbors(K=5):")
predict(LogisticRegression(), "LogisticRegression(defaults):")

