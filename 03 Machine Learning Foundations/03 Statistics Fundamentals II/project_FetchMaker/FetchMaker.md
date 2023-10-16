FetchMaker
Congratulations! You’ve just started working at the hottest new tech startup, FetchMaker. FetchMaker’s mission is to match up prospective dog owners with their perfect pet. FetchMaker has been collecting data on their adoptable dogs, and it’s your job to analyze some of that data.

Note that a solution.py file is also loaded for you in the workspace, which contains solution code for this project. We highly recommend that you complete the project on your own without checking the solution, but feel free to take a look if you get stuck or want to check your answers!

Tasks
11/11 Complete
Mark the tasks as complete by checking them off
Data to the Rescue
1.
FetchMaker has provided us with data for a sample of dogs from their app, including the following attributes:

weight, an integer representing how heavy a dog is in pounds
tail_length, a float representing tail length in inches
age, in years
color, a String such as "brown" or "grey"
is_rescue, a boolean 0 or 1
The data has been saved for you as a pandas DataFrame named dogs. Use the .head() method to inspect the first five rows of the dataset.


Stuck? Get a hint
2.
FetchMaker estimates (based on historical data for all dogs) that 8% of dogs in their system are rescues.

They would like to know if whippets are significantly more or less likely than other dogs to be a rescue.

Store the is_rescue values for 'whippet's in a variable called whippet_rescue.


Stuck? Get a hint
3.
How many whippets are rescues (remember that the value of is_rescue is 1 for rescues and 0 otherwise)? Save this number as num_whippet_rescues and print it out.


Stuck? Get a hint
4.
How many whippets are in this sample of data in total? Save this number as num_whippets and print it out.


Stuck? Get a hint
5.
Use a hypothesis test to test the following null and alternative hypotheses:

Null: 8% of whippets are rescues
Alternative: more or less than 8% of whippets are rescues
Save the p-value from this test as pval and print it out. Using a significance threshold of 0.05, Is the proportion of whippets who are rescues significantly different from 8%?


Stuck? Get a hint
Mid-Sized Dog Weights
6.
Three of FetchMaker’s most popular mid-sized dog breeds are 'whippet's, 'terrier's, and 'pitbull's. Is there a significant difference in the average weights of these three dog breeds?

To start answering this question, save the weights of each of these breeds in three separate series named wt_whippets, wt_terriers, and wt_pitbulls, respectively.


Stuck? Get a hint
7.
Run a single hypothesis test to address the following null and alternative hypotheses:

Null: whippets, terriers, and pitbulls all weigh the same amount on average
Alternative: whippets, terriers, and pitbulls do not all weigh the same amount on average (at least one pair of breeds has differing average weights)
Save the resulting p-value as pval and print it out. Using a significance threshold of 0.05, is there at least one pair of dog breeds that have significantly different average weights?


Stuck? Get a hint
8.
If you completed the previous step correctly, you should have concluded that at least one pair of dog breeds have significantly different average weights.

Run another hypothesis test to determine which of those breeds (whippets, terriers, and pitbulls) weigh different amounts on average. Use an overall type I error rate of 0.05 for all three comparisons. Note that we’ve already provided you with code in script.py to subset the data to just these breeds and have saved this subset as dogs_wtp using the following code:

dogs_wtp = dogs[dogs.breed.isin(['whippet', 'terrier', 'pitbull'])]
This should make it easier for you to run the test you need!

Print out the results. Which pairs of dog breeds weigh different amounts?


Stuck? Get a hint
Poodle and Shihtzu Colors
9.
FetchMaker wants to know if 'poodle's and 'shihtzu's come in different colors. Note that we’ve already provided you with code in script.py to subset the data to just these breeds and have saved this subset as dogs_ps using the following code:

dogs_ps = dogs[dogs.breed.isin(['poodle', 'shihtzu'])]
This should make it easier for you to investigate this question!

To start, use the subsetted data to create a contingency table of dog colors by breed (poodle vs. shihtzu). Save the table as Xtab and print it out.


Stuck? Get a hint
10.
Run a hypothesis test for the following null and alternative hypotheses:

Null: There is an association between breed (poodle vs. shihtzu) and color.
Alternative: There is not an association between breed (poodle vs. shihtzu) and color.
Save the p-value as pval and print it out. Do poodles and shihtzus come in significantly different color combinations? Use a significance threshold of 0.05.


Stuck? Get a hint
Good learner! Have a treat!
11.
Great job!

Feel free to play around with the FetchMaker data some more and run some hypothesis tests of your own.

The breeds you can explore are "poodle", "rottweiler", "whippet", "greyhound", "terrier", "chihuahua", "shihtzu", and "pitbull".

Extra challenge: Remind yourself of your data visualization skills and your ability to describe the central tendency of the data. For example, a boxplot visualization can add a lot to your understanding of an ANOVA result.