import pandas as pd
#import codecademylib3
from surprise import Reader

book_ratings = pd.read_csv('goodreads_ratings.csv')
print(book_ratings.head())

#1. Print dataset size and examine column data types
print(book_ratings.info())

#2. Distribution of ratings
print(book_ratings['rating'].value_counts())

#3. Filter ratings that are out of range
book_ratings = book_ratings[book_ratings['rating']!=0]
print(book_ratings['rating'].value_counts())

#4. Prepare data for surprise: build a Suprise reader object
from surprise import Reader
reader = Reader(rating_scale=(1,5))

#5. Load `book_ratings` into a Surprise Dataset
from surprise import Dataset
dataset = Dataset.load_from_df(book_ratings[['user_id','book_id','rating']], reader)

#6. Create a 80:20 train-test split and set the random state to 7
from surprise.model_selection import train_test_split
trainset, testset = train_test_split(dataset, test_size=.2, random_state=7)

#7. Use KNNBasice from Surprise to train a collaborative filter
from surprise import KNNBasic
book_recommender = KNNBasic()
book_recommender.fit(trainset)

#8. Evaluate the recommender system
from surprise import accuracy
predictions = book_recommender.test(testset)
print(predictions[0])
accuracy.rmse(predictions)

#9. Prediction on a user who gave the "The Three-Body Problem" a rating of 5
print('---')
print("prediction for 3 body problem...")
from surprise import SVD
svd_recommender = SVD()
svd_recommender.fit(trainset)

svd_predictions = svd_recommender.test(testset)

accuracy.rmse(svd_predictions)