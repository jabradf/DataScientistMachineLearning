Determining Significance
Now that we’ve practiced simulating data for an A/B test, let’s actually run a Chi-Square test for each simulated dataset and consider the decision we would make based on the outcome.

If we were really running this test, we would want to use the data to make a decision about whether to use the control (old) or name (new) email subject. To make that decision, we can use a significance threshold. For example, if we’re using a significance threshold of 0.05, we’ll “reject the null hypothesis” for any p-value less than 0.05. In this context, rejecting the null would mean that we conclude that there is a significant difference between the open rates for the two email subjects and therefore we should switch to the email subject that uses the recipient’s first name.

We can use the following Python statement to record whether a particular p-value is significant or not, based on a threshold of 0.05:

result = ('significant' if pval < 0.05 else 'not significant')
print(result)