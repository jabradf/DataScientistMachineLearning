Analyzing Farmburg's A/B Test
Brian is a Product Manager at FarmBurg, a company that makes a farming simulation social network game. In the FarmBurg game, you can plow, plant, and harvest different crops. ​Brian has been conducting an A/B Test with three different variants, and he wants you to help him analyze the results. Using the Python modules pandas and SciPy, you will help him make some important business decisions!

Note that a solution.py file is also loaded for you in the workspace, which contains solution code for this project. We highly recommend that you complete the project on your own without checking the solution, but feel free to take a look if you get stuck or want to check your answers!

Tasks
13/13 Complete
Mark the tasks as complete by checking them off
Project Requirements
1.
Brian ran an A/B test with three different groups: A, B, and C. He has provided us with a CSV file of his results named clicks.csv. It has the following columns:

user_id: a unique id for each visitor to the FarmBurg site
group: either 'A', 'B', or 'C' depending on which group the visitor was assigned to
is_purchase: either 'Yes' if the visitor made a purchase or 'No' if they did not.
We’ve already imported pandas as pd and loaded clicks.csv as abdata. Inspect the data using the .head() method.


Stuck? Get a hint
2.
Note that we have two categorical variables: group and is_purchase. We are interested in whether visitors are more likely to make a purchase if they are in any one group compared to the others. Because we want to know if there is an association between two categorical variables, we’ll start by using a Chi-Square test to address our question.

In order to run a Chi-Square test, we first need to create a contingency table of the variables group and is_purchase. Use pd.crosstab() to create this table and name the result Xtab, then print it out. Which group appears to have the highest number of purchases?


Stuck? Get a hint
3.
To conduct the Chi-Square Test, import chi2_contingency from scipy.stats.

Then, use the function chi2_contingency with the data in Xtab to calculate the p-value. Remember that of the four values returned by chi2_contingency, the p-value is the second value.

Save the p-value to a variable named pval and print the result. Using a significance threshold of 0.05, is there a significant difference in the purchase rate for groups A, B, and C?

Note that you might see a number in scientific notation. For example, 1.234e-8 is equal to 0.00000001234 (we move the decimal to the left by 8 places and insert zeros).


Stuck? Get a hint
4.
Our day is a little less busy than expected, so we decide to ask Brian about his test.

Us: Hey Brian! What was that test you were running anyway?

Brian: We are trying to get users to purchase a small FarmBurg upgrade package. It’s called a microtransaction. We’re not sure how much to charge for it, so we tested three different price points: $0.99 (group 'A'), $1.99 (group 'B'), and $4.99 (group 'C'). It looks like significantly more people bought the upgrade package for $0.99, so I guess that’s what we’ll charge.

Us: Oh no! We should have asked you this before we did that Chi-Square test. That wasn’t the right test at all. It’s true that more people wanted to purchase the upgrade at $0.99; you probably expected that. What we really want to know is whether each price point allows us to make enough money that we can exceed some target goal. Brian, how much do you think it cost to build this feature?

Brian: Hmm. I guess that we need to generate a minimum of $1000 in revenue per week in order to justify this project.

Us: We have some work to do!

In order to justify this feature, we will need to calculate the necessary purchase rate for each price point. Let’s start by calculating the number of visitors to the site this week.

It turns out that Brian ran his original test over the course of a week, so the number of visitors in abdata is equal to the number of visitors in a typical week. Calculate the number of visitors in the data and save the value in a variable named num_visits. Make sure to print the value.


Stuck? Get a hint
5.
Now that we know how many visitors we generally get each week (num_visits), we need to calculate the number of visitors who would need to purchase the upgrade package at each price point ($0.99, $1.99, $4.99) in order to generate Brian’s minimum revenue target of $1,000 per week.

To start, calculate the number of sales that would be needed to reach $1,000 dollars of revenue at a price point of $0.99. Save the result as num_sales_needed_099 and print it out.


Stuck? Get a hint
6.
Now that we know how many sales we need at a $0.99 price point, calculate the proportion of weekly visitors who would need to make a purchase in order to meet that goal. Remember that the number of weekly visitors is saved as num_visits. Save the result as p_sales_needed_099 and print it out.


Stuck? Get a hint
7.
Repeat the steps from tasks 5 and 6 for the other price points ($1.99 and $4.99). Save the number of sales needed for each price point as num_sales_needed_199 and num_sales_needed_499, respectively. Then, save the proportion of visits needed as p_sales_needed_199 and p_sales_needed_499, respectively.

Print out the proportions. Note that for higher price points, you’ll need to sell fewer upgrade packages in order to meet your minimum revenue target — so the proportions should decrease as the price points increase.


Stuck? Get a hint
8.
Now let’s return to Brian’s question. To start, we want to know if the percent of Group A (the $0.99 price point) that purchased an upgrade package is significantly greater than p_sales_needed_099 (the percent of visitors who need to buy an upgrade package at $0.99 in order to make our minimum revenue target of $1,000).

To answer this question, we want to focus on just the visitors in group A. Then, we want to compare the number of purchases in that group to p_sales_needed_099.

Since we have a single sample of categorical data and want to compare it to a hypothetical population value, a binomial test is appropriate. In order to run a binomial test for group A, we need to know two pieces of information:

The number of visitors in group A (the number of visitors who were offered the $0.99 price point)
The number of visitors in Group A who made a purchase
Calculate these two numbers and save them as samp_size_099 and sales_099, respectively. Note that you can use the contingency table that you printed earlier to get these numbers OR you can use Python syntax.


Stuck? Get a hint
9.
Calculate the sample size and number of purchases in group B (the $1.99 price point) and save them as samp_size_199 and sales_199, respectively. Then do the same for group C (the $4.99 price point) and save them as samp_size_499 and sales_499, respectively.


Stuck? Get a hint
10.
For Group A ($0.99 price point), perform a binomial test using binom_test() to see if the observed purchase rate is significantly greater than p_sales_needed_099. Remember that there are four inputs to binom_test():

x will be the number of purchases for Group A
n will be the total number of visitors assigned group A
p will be the target percent of purchases for the $0.99 price point
alternative will indicate the alternative hypothesis for this test; in this case, we want to know if the observed purchase rate is significantly 'greater' than the purchase rate that results in the minimum revenue target.
Save the results to pvalueA, and print its value. Note that you’ll first need to import the binom_test() function from scipy.stats using the following line of code:

from scipy.stats import binom_test

Stuck? Get a hint
11.
For Group B ($1.99 price point), perform a binomial test to see if the observed purchase rate is significantly greater than p_sales_needed_199.

Save the results to pvalueB, and print its value.


Stuck? Get a hint
12.
For Group C ($4.99 price point), perform a binomial test to see if the observed purchase rate is significantly greater than p_sales_needed_499.

Save the results to pvalueC, and print its value.


Stuck? Get a hint
13.
Based on the three p-values you calculated for the binomial tests in each group and a significance threshold of 0.05, were there any groups where the purchase rate was significantly higher than the target? Based on this information, what price should Brian charge for the upgrade package?