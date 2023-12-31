DATA SCIENCE FOUNDATIONS II
Heart Disease Research Part I
In this project, you’ll investigate some data from a sample patients who were evaluated for heart disease at the Cleveland Clinic Foundation. The data was downloaded from the UCI Machine Learning Repository and then cleaned for analysis. The principal investigators responsible for data collection were:

Hungarian Institute of Cardiology. Budapest: Andras Janosi, M.D.
University Hospital, Zurich, Switzerland: William Steinbrunn, M.D.
University Hospital, Basel, Switzerland: Matthias Pfisterer, M.D.
V.A. Medical Center, Long Beach and Cleveland Clinic Foundation: Robert Detrano, M.D., Ph.D.
Note that a solution.py file is loaded for you in the workspace, which contains solution code for this project. We highly recommend that you complete the project on your own without checking the solution, but feel free to take a look if you get stuck or want to check your answers when you’re done!

Tasks
10/10 Complete
Mark the tasks as complete by checking them off
Cholesterol Analysis
1.
The full dataset has been loaded for you as heart, then split into two subsets:

yes_hd, which contains data for patients with heart disease
no_hd, which contains data for patients without heart disease
For this project, we’ll investigate the following variables:

chol: serum cholestorol in mg/dl
fbs: An indicator for whether fasting blood sugar is greater than 120 mg/dl (1 = true; 0 = false)
To start, we’ll investigate cholesterol levels for patients with heart disease. Use the dataset yes_hd to save cholesterol levels for patients with heart disease as a variable named chol_hd.


Stuck? Get a hint
2.
In general, total cholesterol over 240 mg/dl is considered “high” (and therefore unhealthy). Calculate the mean cholesterol level for patients who were diagnosed with heart disease and print it out. Is it higher than 240 mg/dl?


Stuck? Get a hint
3.
Do people with heart disease have high cholesterol levels (greater than or equal to 240 mg/dl) on average? Import the function from scipy.stats that you can use to test the following null and alternative hypotheses:

Null: People with heart disease have an average cholesterol level equal to 240 mg/dl
Alternative: People with heart disease have an average cholesterol level that is greater than 240 mg/dl
Note: Unfortunately, the scipy.stats function we’ve been using does not (at the time of writing) have an alternative parameter to change the alternative hypothesis for this test. Therefore, you’ll have to run a two-sided test. However, since you calculated earlier that the average cholesterol level for heart disease patients is greater than 240 mg/dl, you can calculate the p-value for the one-sided test indicated above simply by dividing the two-sided p-value in half.


Stuck? Get a hint
4.
Run the hypothesis test indicated in task 3 and print out the p-value. Can you conclude that heart disease patients have an average cholesterol level significantly greater than 240 mg/dl? Use a significance threshold of 0.05.


Stuck? Get a hint
5.
Repeat steps 1-4 in order to run the same hypothesis test, but for patients in the sample who were not diagnosed with heart disease. Do patients without heart disease have average cholesterol levels significantly above 240 mg/dl?


Stuck? Get a hint
Fasting Blood Sugar Analysis
6.
Let’s now return to the full dataset (saved as heart). How many patients are there in this dataset? Save the number of patients as num_patients and print it out.


Stuck? Get a hint
7.
Remember that the fbs column of this dataset indicates whether or not a patient’s fasting blood sugar was greater than 120 mg/dl (1 means that their fasting blood sugar was greater than 120 mg/dl; 0 means it was less than or equal to 120 mg/dl).

Calculate the number of patients with fasting blood sugar greater than 120. Save this number as num_highfbs_patients and print it out.


Stuck? Get a hint
8.
Sometimes, part of an analysis will involve comparing a sample to known population values to see if the sample appears to be representative of the general population.

By some estimates, about 8% of the U.S. population had diabetes (diagnosed or undiagnosed) in 1988 when this data was collected. While there are multiple tests that contribute to a diabetes diagnosis, fasting blood sugar levels greater than 120 mg/dl can be indicative of diabetes (or at least, pre-diabetes). If this sample were representative of the population, approximately how many people would you expect to have diabetes? Calculate and print out this number.

Is this value similar to the number of patients with a resting blood sugar above 120 mg/dl — or different?


Stuck? Get a hint
9.
Does this sample come from a population in which the rate of fbs > 120 mg/dl is equal to 8%? Import the function from scipy.stats that you can use to test the following null and alternative hypotheses:

Null: This sample was drawn from a population where 8% of people have fasting blood sugar > 120 mg/dl
Alternative: This sample was drawn from a population where more than 8% of people have fasting blood sugar > 120 mg/dl

Stuck? Get a hint
10.
Run the hypothesis test indicated in task 9 and print out the p-value. Using a significance threshold of 0.05, can you conclude that this sample was drawn from a population where the rate of fasting blood sugar > 120 mg/dl is significantly greater than 8%?