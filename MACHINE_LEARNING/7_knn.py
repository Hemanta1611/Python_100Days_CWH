from sklearn import datasets
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier as KNC

# Loading Dataset
iris = load_iris()


# Printing description and features
print(iris.DESCR)
features = iris.data
labels = iris.target
print(features[0], labels[0]) # have 4 features and 1 labels


# Training the classifiers
clf = KNC()
clf.fit(features, labels)
preds = clf.predict([[5.1, 3.5, 1.4, 0.2]])
print(preds)

