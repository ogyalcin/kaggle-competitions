results = ids.assign(Survived = predictions) # assign predictions to ids
results.to_csv("titanic-results.csv", index=False) # write the final dataset to a csv file.