import pandas as pd
train = pd.read_csv("train.csv")
train = train.dropna()
y = train['Survived']
X = train.drop(['Survived', 'PassengerId', 'Name', 'Ticket', 'Cabin'], 1, inplace=True)
X = pd.get_dummies(train)

from sklearn import tree
dtc = tree.DecisionTreeClassifier()
dtc.fit(X, y)

test = pd.read_csv("test.csv")
ids = test[['PassengerId']]
test.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], 1, inplace=True)
test.fillna(2, inplace=True)
test = pd.get_dummies(test)

predictions = dtc.predict(test)

results = ids.assign(Survived = predictions)
results.to_csv("titanic-results.csv", index=False)
