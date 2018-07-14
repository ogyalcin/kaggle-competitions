import pandas as pd
train = pd.read_csv("train.csv") #load the data from the system
train = train.dropna() #delete the rows with empty values
y = train['Survived'] #select the column representing survival 
X = train.drop(['Survived', 'PassengerId', 'Name', 'Ticket', 'Cabin'], 1, inplace=True) # drop the irrelevant columns and keep the rest
X = pd.get_dummies(train) # convert non-numerical variables to dummy variables