# Types of Missing Data
## Why are there different types of missing data?

Just as data goes missing for different reasons, there are different ways in which it is missing.

For the rest of this article, we’ll imagine we have a dataset from a health survey campaign that we ran in our local area. These surveys requested basic information about each person, and participation was completely voluntary.

When trying to decide what kind of missing data we have, there are two factors we have to take into account:
### How important is this data to the larger dataset?
While every variable in a dataset can provide some information that we need, not all variables are created equal. Depending on what we are trying to learn, some fields have more importance than others. It seems obvious that we can’t use data that doesn’t fit our questions – but you’d be surprised how often we accidentally try to.

For example, let’s imagine we are collecting data for a health survey. We are collecting activity level (measured in minutes), location (city), and blood pressure. If we are missing a lot of data on blood pressure, then we can’t use that dataset to answer questions about blood pressure. We can still use it to understand the relationship between location and activity, but not blood pressure. 

## Different types of missing data

But there’s more to missing data than missingness. Missing data comes in four varieties:

* __Structurally Missing Data__ we expect this data to be missing for some logical reason
* __Missing Completely at Random (MCAR)__ the probability of any datapoint being MCAR is the same for all data points – this type of missing data is mostly hypothetical
* __Missing at Random (MAR)__ the probability of any data point being MAR is the same within groups of the observed data – this is much more realistic than MCAR
* __Missing Not at Random (MNAR)__ there is some reason why the data is missing

Let’s dive into some more details about these types of nothing.
### Structurally Missing Data

![doughnut](./img/doughnut.png)
Sometimes when we have missing data, we aren’t surprised at all. In fact, in some scenarios, we should have missing data, because it makes sense! This is what Structurally Missing Data is, and it frequently occurs when there are one or more fields that depend on another.

Let’s say that a section of our health survey is asking about common respiratory conditions, and we see a section in our data that look like the following:

```
articipantID 	AsthmaFlag 	InhalerFrequency 	InhalerBrand
100 	TRUE 	Twice daily 	Breathe-Rite
101 	TRUE 	Once weekly 	Breathe-Rite
102 	FALSE 		
103 	TRUE 	Once daily 	    Asthm-Away
104 	FALSE 		
```

As we can see, two rows do not have any data for the frequency and brand. This is expected since we see in the `AsthmaFlag` field that these participants do not use an inhaler at all.

### Missing Completely at Random (MCAR)
![dice](./img/dice.png)

Sometimes data is just missing. It can happen for any reason, but the important thing is that it could have happened to any observation. For a given variable, every observation is equally likely to be missing. Beyond that, MCAR data is truly only MCAR if every potential observation is equally likely to be missing a value for that variable.

There’s no logic, no outside force, or unseen behavior. It’s just a completely random, fluke occurrence that there isn’t data. MCAR data demands statistical perfection, which is extremely rare because more often than not, there is some unseen reason why data might be missing.

But let’s imagine our health survey data again. Steps are part of activity minutes, and let’s say there is a bug in the software that causes the device to not record steps. It’s completely random if someone has the bug in their device or not, and we know from the developers that about 20% of devices are affected. Therefore, we might expect that any missing step counts are MCAR. The below data shows a sampling of our data:

| ParticipantID | Walked | Steps (1,000) |
|:-------------:|:------:|:-------------:|
| 25            | TRUE   | 2.1           |
| 43            | TRUE   | 15            |
| 61            | TRUE   | 6             |
| 62            | TRUE   |               |
| 78            | TRUE   | 3             |
| 84            | TRUE   |               |
| 90            | TRUE   | 0.5           |
| 102           | TRUE   | 1.5           |
| 110           | TRUE   | .01           |
| 115           | TRUE   | 4.1           |

Since all of these people have identified that they walked on that day, we can assume that the value for `Steps` should not be missing. We also know about this bug, and see that about 20% of our respondents are recording no steps. Therefore we may be able to assume that the missing values are simply missing by chance, and there isn’t an underlying reason for the missingness (this is actually a really big assumption – but we know about the bug, so seems ok).

This kind of missing data is less impactful on our analytics than other types, as there are a variety of techniques we can use to increase the accuracy of our analysis. We could impute the data by taking the average number of steps. We could interpolate the data by generating values based on the distribution of the existing data. Or we could delete it without making our analysis invalid.

### Missing at Random (MAR)
![rubiks cube](./img/rubiks_cube.png)

Missing at Random might be the most complex of the missing data types. If the likelihood of missingness is different for different groups, but equally likely within a group, then that data is missing at random. It’s kind of a hybrid of missing for a reason and missing completely at random.

For example, several scientific studies have shown that individuals do not like to report their weight, especially when they have a Body Mass Index (BMI) outside of the “normal” range (normal is in quotations because [BMI is a questionable statistic](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2930234/) and “normal” is poorly defined, but is the label BMI scales typically use). In our study, we asked participants to report their `height` and `weight`.

This is an example of Missing at Random data because we can assume that some groups are not reporting their weight for a reason, but that anyone within that group (i.e., someone with a non-“normal” BMI) has an equal probability of not reporting their weight.

Let’s look at a sampling of our survey data.

| ParticipantID | Height (cm) | Weight (kg) |
|:-------------:|:-----------:|:-----------:|
| 1             | 176         | 84          |
| 2             | 190         |             |
| 3             | 160         | 61          |
| 4             | 180         |             |
| 5             | 184         |             |
| 6             | 158         | 72          |
| 7             | 152         | 50          |
| 8             | 156         |             |
| 9             | 194         | 104         |
| 10            | 180         | 79          |



As we can see, some data is missing. Since we know that some people don’t like to report weight, and we also know that not everyone feels that way, and it doesn’t apply to our entire population, this data is Missing At Random (we know that this is not what “random” usually means, but it’s the statistical definition).

This will impact our analysis and limits the claims we are able to make, but there still are several techniques we can still employ that will allow us to use the data that was reported.

### Missing Not at Random (MNAR)
![containers](./img/containers.png)
Finally, sometimes data is missing for a good reason that applies to all of the data. This can be the most interesting type because it’s when missingness actually tells its own story. This is when the value of the missing variable is related to the reason it’s missing in the first place!

Let’s walk through an example to better understand MNAR. Participants in our study have been assigned to a local clinic to get a health reading. They will get blood pressure, height, and weight measured, and the clinician will enter notes after an interview. But a portion of the weight measurements are missing. Participants weren’t responsible for self-reporting, so this is unexpected. We might assume that they didn’t want to be weighed, but if we dive deeper into the data, we might get a different picture. We try the following groupings:

1. last-reported weight to see if data is missing from higher or lower BMI groups
2. demographics such as age, race, and gender to see if there is a pattern here
3. date of data collection

Let’s say we discovered that the missing data was all collected on the same day. In our clinic, the scales are battery-operated. If the scale runs out of batteries, someone will have to buy more. The data is missing for a reason, even though that reason is completely unrelated to our study.

It’s best practice to always assume that the data is MNAR and try to uncover clues as to that reason. As the analyst, you will probably never truly know why data is missing, but finding a pattern can often inform whether the MNAR data is important to your study or not. And knowing that can help you decide what to do about the missing data.

## Data about Data
When trying to diagnose the type of missingness, data about the data (aka meta data) can be invaluable. The date/time data was collected, how it was collected, who collected it, where it was collected, etc. can all give invaluable clues to solving the problem of missing data.

In the end, a lot of data analytics type work is solving mysteries, and The Mystery of the Missing Data is one of the best sellers.
