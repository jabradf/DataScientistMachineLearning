from movies import movie_dataset, movie_ratings
from sklearn.neighbors import KNeighborsRegressor
import numpy as np

regressor = KNeighborsRegressor(n_neighbors = 5, weights = "distance")

regressor.fit(movie_dataset, movie_ratings)

unknown_points = np.array([[0.016, 0.300, 1.022], [0.0004092981, 0.283, 1.0112], [0.00687649, 0.235, 1.0112]])
 
guesses = regressor.predict(unknown_points)

print(guesses)

#online course prints:
# [6.84913968 5.47572913 6.91067999]