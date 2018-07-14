test = pd.read_csv("test.csv") # load the testing data
ids = test[['PassengerId']] # create a sub-dataset for submission file and saving it
test.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], 1, inplace=True) # drop the irrelevant and keeping the rest
test.fillna(2, inplace=True) # fill (instead of drop) empty rows so that I would get the exact row number required for submission
test = pd.get_dummies(test) # convert non-numerical variables to dummy variables