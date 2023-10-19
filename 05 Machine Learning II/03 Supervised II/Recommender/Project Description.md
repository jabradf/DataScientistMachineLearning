Build a Book Recommender System
Recommender systems are used in all sorts of organizations to help users make decisions and, for many companies, earn more revenue. Prototyping simple recommender systems also does not need to take a lot of time. In this project, we will build a book recommender system for Books’R’Us using Surprise.

Books’R’Us is a national bookstore chain that sells books of all sorts to people all over the country. They recently have built their website, and now want to add a book recommender system to their site. We will prepare and train the recommender system using book review data left on their site. This data has been put together in a Pandas DataFrame called book_ratings.

Tasks
10/10 Complete
Mark the tasks as complete by checking them off
Prepare your data for recommender implementation
1.
Take a sneak peek into the dataset by printing the first five rows. How big is the dataset? What are the data types of the different fields?


Stuck? Get a hint
2.
In order to understand these ratings, let’s look at a count of all the ratings in the data. Examine the distribution of the ratings using value_counts.


Hint
Use book_ratings['rating'].value_counts().

3.
Unfortunately, it appears we have some data where the ratings are 0. The ratings on the website only go from 1 to 5 inclusive. Filter out all ratings that are not in this range.


Hint
You can filter for book_ratings['ratings']!=0.

4.
We need to prepare this data for use in Surprise. First, build a Surprise reader Object that utilizes the rating scale established above. Look at the Surprise documentation to help you out.


Stuck? Get a hint
Build a recommender system using `Surprise`
5.
Load book_ratings into a Surprise Dataset so it can be used with Surprise‘s algorithms.


Stuck? Get a hint
6.
We have a dataset that is ready for use in Surprise. Split the data, and put 80% of the data into a training set, and 20% into a test set. Set a random_state of 7 to improve reproducibility.


Stuck? Get a hint
7.
We can finally train a recommender system. Use the KNNBasic from Surprise to train a collaborative filter using the training set.


Stuck? Get a hint
8.
How good is the algorithm we trained? Calculate the RMSE of the recommender system using the testset data.

9.
Time to get a recommendation! User 8842281e1d1347389f2ab93d60773d4d gave the science-fiction book “The Three-Body Problem” (book_id=18245960) a 5. What rating does the algorithm predict this user will give the science-fiction book “The Martian” (book_id=18007564)?

10.
We have successfully built a working prototype for a recommender system. Try adjusting the hyperparameters of the collaborative filter you built, and see if you can reduce the RMSE of the collaborative filter you built above.