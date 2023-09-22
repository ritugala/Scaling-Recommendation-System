import pandas as pd
from surprise.reader import Reader
from surprise import Dataset, dump
from surprise import SVD, accuracy
from surprise import NMF
from surprise.model_selection import train_test_split


df = pd.read_csv("meow.csv")
df =df.sort_values('time')
reader = Reader(rating_scale=(1, 5))
data = Dataset.load_from_df(df[["user id", "movie id", "rating"]], reader=reader)
trainset, testset = train_test_split(data, test_size=0.15, random_state=0, shuffle=False)
algorithm_svd = SVD()
algorithm_svd.fit(trainset)
predictions = algorithm_svd.test(testset)
accuracy.rmse(predictions)

print("RMSE is: ", accuracy)