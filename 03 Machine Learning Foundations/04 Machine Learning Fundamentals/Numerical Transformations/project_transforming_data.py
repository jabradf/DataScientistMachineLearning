import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

#import data
review = pd.read_csv('reviews.csv')
 
#print column names
#print .info
print(review.info())

#look at the counts of recommended
print("counts of review:\n",review.recommended.value_counts())
 
#create binary dictionary
binary_dict = {True:1, False:0}
 
#transform column
review['recommended'] = review['recommended'].map(binary_dict)
 
#print your transformed column
print("counts of transformed data, should match previous results!")
 
#print your transformed column
print(review['recommended'].value_counts())

#look at the counts of rating
print("counts of rating:\n",review.rating.value_counts())
 
#create dictionary
rating_dict = {"Loved it":5,
  "Liked it":4,
  "Was okay":3,
  "Not great":2,
  "Hated it":1}
 
#transform rating column
review['rating'] = review['rating'].map(rating_dict)
 
#print your transformed column values
print("transformed counts of rating:\n",review.rating.value_counts())

#get the number of categories in a feature
print(review.department_name.value_counts())
 
#perform get_dummies (one hot encoding)
one_hot = pd.get_dummies(review['department_name'])
# can also use: one_hot = pd.get_dummies(review['department_name'], drop_first=True)
# drop_first reduces redundant data
 
#join the new columns back onto the original
review = review.join(one_hot)

#print column names
print(review.info())

#transform review_date to date-time data
review['review_date'] = pd.to_datetime(review['review_date'])

#print review_date data type 
print("datatype of datetime column:",review['review_date'].dtype)

#get numerical columns
reviews_numerical = review[['clothing_id', 'age', 'recommended', 'rating', 'Bottoms', 'Dresses', 'Intimate', 'Jackets', 'Tops', 'Trend']].copy()
 
#reset index
#print(reviews_numerical.head())
reviews_numerical = reviews_numerical.set_index('clothing_id')

#instantiate standard scaler
scaler = StandardScaler()
 
#fit transform data
scaler.fit_transform(reviews_numerical)
