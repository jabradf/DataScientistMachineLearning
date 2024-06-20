# Single Imputation

Filling in the blanks one at a time

Imagine: you are watching a stock ticker for your favorite company, hoping for it to drop in price so you can jump at the opportunity to invest. Each minute goes by, and it creeps lower and lower, almost to where we want it. Then, suddenly, the data is gone! Then, just as quickly as it disappeared, the price is back, and it has gone up again! What could have happened here?

## What is time-series data?
The stock ticker data we were watching is called a time-series dataset. These datasets have interesting properties and analytics capabilities because they track data over (usually) set periods of time. If we are missing data in one of these periods, we have a variety of unique approaches to handle this missing data.

When data is missing in time-series data, we have the advantage of context. That is, because the data shows observations of the same event over time, we can learn about what is happening and make an educated guess as to what might have happened in our missing data. The methods that we will talk about in this article are specific to time-series data because of this property.

# Is it MNAR?

Before we can start describing techniques, we must verify that our missing data can be categorized as MNAR — these techniques assume that to be the case. It can be tricky to understand that the data is missing in a non-random manner. How exactly can we verify this? There are two key aspects to be able to accurately describe missing data as MNAR:

1. __Use domain knowledge__: Probably the quickest way to identify MNAR is by having extensive knowledge of the data and industry we are working in. Missing data that falls into MNAR will look and feel different from “normal” data in our dataset.

    With domain knowledge, either from ourselves or someone on our team, we could identify the cause for missing data. For example, someone might know that data in a survey is missing in a particular column because the participant was either too embarrassed to answer, or didn’t know the answer. This would let us know that the data is MNAR.

2. __Analyze the dataset to find patterns__: As we explore, filter, and separate our data, we should ultimately be able to identify something about our missing data that doesn’t line up with everything else. For example, if we have some survey data, we might find that our missing data almost exclusively comes from men older than 55 years old. If we see a pattern like this emerge, we can confidently say it is MNAR.

## What can we do?
Now that we have identified the missing data as MNAR, what can we do to handle our missing data? Let’s take a look at an example of missing data in a time series:

|     Timestamp    | Value |
|:----------------:|:-----:|
| 01/10/2021 08:01 | 12    |
| 01/10/2021 08:02 | 13    |
| 01/10/2021 08:03 |       |
| 01/10/2021 08:04 | 16    |
| 01/10/2021 08:05 | 15    |

In this case, our dataset has a value for every minute, and we are missing one value. The best way to handle this missing data is by using the data around it to “fill in the blanks”. This is called single imputation, and there are many ways that we can tackle this problem.

## LOCF
LOCF stands for Last Observation Carried Forward. With this technique, we are going to fill in the missing data with the previous value. LOCF is used often when we see a relatively consistent pattern that has continued to either increase or decrease over time.

Let’s look at the below dataset with data about how comfortable an office location is, from a collection of employees wearing smartwatches. This data has been adapted from [this “Longitudinal indoor personal comfort preferences” Kaggle dataset](https://www.kaggle.com/claytonmiller/longitudinal-personal-thermal-comfort-preferences) for the purposes of this article.

|            time           | space_id |  comfort  |
|:-------------------------:|:--------:|:---------:|
| 2021-03-16 08:22:00+08:00 | 125      | Comfy     |
| 2021-03-16 09:37:00+08:00 | 125      | Not Comfy |
| 2021-03-18 08:11:00+08:00 | 125      | Not Comfy |
| 2021-03-18 09:48:00+08:00 | 125      | Comfy     |
| 2021-03-18 13:35:00+08:00 | 125      | Comfy     |
| 2021-03-18 15:23:00+08:00 | 125      | Comfy     |
| 2021-03-18 15:53:00+08:00 | 125      |           |
| 2021-03-18 18:58:00+08:00 | 125      | Comfy     |
| 2021-03-19 08:05:00+08:00 | 125      | Not Comfy |
| 2021-03-19 09:53:00+08:00 | 125      | Comfy     |

We see that there is a missing value in the seventh row at `2021-03-18 15:53:00+08:00` for the overall comfort of the office in this particular space. Since we are looking at data for an office space, we can assume that there wouldn’t be a big change in overall comfort in the span of thirty minutes. This makes the dataset a good candidate for LOCF.

In Python, there are a variety of methods we can employ:

1. If your data is in a pandas DataFrame, we can use the `.ffil()` method on a particular column:
```py
df['comfort'].ffill(axis=0, inplace=True)
# Applying Forward Fill (another name for LOCF) on the comfort column
```

2. If our data is in a NumPy array, there is a commonly used library called [impyute](https://impyute.readthedocs.io/en/master/index.html) that has a variety of time-series functions. To use LOCF, we can write the following code:
```py
impyute.imputation.ts.locf(data, axis=0)
# Applying LOCF to the dataset
```


With both of these methods, we are looking to carry data in the `comfort` column forward to fill in our missing data. In this case, we want to move our `Comfy` value from the previous timestamp to fill in our missing data. Thus, our dataset would now look like this:

|            time           | space_id |  comfort  |
|:-------------------------:|:--------:|:---------:|
| 2021-03-16 08:22:00+08:00 | 125      | Comfy     |
| 2021-03-16 09:37:00+08:00 | 125      | Not Comfy |
| 2021-03-18 08:11:00+08:00 | 125      | Not Comfy |
| 2021-03-18 09:48:00+08:00 | 125      | Comfy     |
| 2021-03-18 13:35:00+08:00 | 125      | Comfy     |
| 2021-03-18 15:23:00+08:00 | 125      | Comfy     |
| 2021-03-18 15:53:00+08:00 | 125      | Comfy     |
| 2021-03-18 18:58:00+08:00 | 125      | Comfy     |
| 2021-03-19 08:05:00+08:00 | 125      | Not Comfy |
| 2021-03-19 09:53:00+08:00 | 125      | Comfy     |

  

This dataset is a good candidate for LOCF, since the data before our missing data has a consistent trend (the office is `Comfy` for six hours before our missing data). LOCF is a great method when we can assume that past data will carry forward.

## NOCB

NOCB stands for Next Observation Carried Backward, and it solves imputation in the opposite direction of LOCF. NOCB is usually used when we have more recent data, and we know enough about the past to fill in the blanks that way. Let’s look again at our office comfort dataset for another space in the office:

|            time           | space_id |  comfort  |
|:-------------------------:|:--------:|:---------:|
| 2021-03-12 14:49:00+08:00 | 2        | Comfy     |
| 2021-03-17 15:30:00+08:00 | 2        | Comfy     |
| 2021-03-17 15:33:00+08:00 | 2        | Comfy     |
| 2021-03-17 15:53:00+08:00 | 2        | Not Comfy |
| 2021-03-18 11:23:00+08:00 | 2        |           |
| 2021-03-18 11:38:00+08:00 | 2        | Comfy     |
| 2021-03-18 12:01:00+08:00 | 2        | Comfy     |
| 2021-03-18 13:49:00+08:00 | 2        | Comfy     |
| 2021-03-18 14:22:00+08:00 | 2        | Comfy     |
| 2021-03-18 15:24:00+08:00 | 2        | Comfy     |
| 2021-03-18 15:59:00+08:00 | 2        | Comfy     |

For this particular space, we are missing the first value for the `comfort` level on March 18th, 2021. Since we can see that the rest of the data for all the data after `2021-03-18 11:23:00+08:00` all share the same value, this dataset would be a good candidate for NOCB.

Similarly to LOCF, there are a couple common techniques we can use:

1. If your data is in a pandas DataFrame, when we can use the `.bfil()` method on a particular column. By “back-filling” (another name for NOCB) our data, we will take data from the next data point in the time series and carry it backwards.
```py
df['comfort'].bfill(axis=0, inplace=True)
```

2. To use `impyute` to perform NOCB, we can write the following code
```py
impyute.imputation.ts.nocb(data, axis=0)
```

In both code blocks, we are trying to take the data

|            time           | space_id |  comfort  |
|:-------------------------:|:--------:|:---------:|
| 2021-03-12 14:49:00+08:00 | 2        | Comfy     |
| 2021-03-17 15:30:00+08:00 | 2        | Comfy     |
| 2021-03-17 15:33:00+08:00 | 2        | Comfy     |
| 2021-03-17 15:53:00+08:00 | 2        | Not Comfy |
| 2021-03-18 11:23:00+08:00 | 2        | Comfy     |
| 2021-03-18 11:38:00+08:00 | 2        | Comfy     |
| 2021-03-18 12:01:00+08:00 | 2        | Comfy     |
| 2021-03-18 13:49:00+08:00 | 2        | Comfy     |
| 2021-03-18 14:22:00+08:00 | 2        | Comfy     |
| 2021-03-18 15:24:00+08:00 | 2        | Comfy     |
| 2021-03-18 15:59:00+08:00 | 2        | Comfy     |

With NOCB, we can use information from more recent entries to fill in data from that past.

# Other alternatives

With LOCF and NOCB, we assume that the data either directly before or after is accurate enough to fill in any surrounding missing data. There are, however, other approaches we can try depending on our data. As with the previous methods of single imputation, deciding which method to use requires domain knowledge to correctly fill in the missing values.

One such alternative is BOCF, or Baseline Observation Carried Forward. In this approach, the initial values for a given variable are applied to missing values. This is a common approach in medical studies, particularly in drug studies. For example, we could assume that missing data for a reported pain level could return to the baseline value. This would happen if a drug were not working as well, so it could be a safe assumption to make if the data is trending in that direction.

Let’s look at an example dataset. In this data, we are trying to study some measure of bacteria in a patient’s body after the patient receives a drug that is supposed to reduce it. Here is a set of dummy data that could represent this:

|      timestamp      | concentration |
|:-------------------:|:-------------:|
| 2021-09-01 08:00:00 | 100           |
| 2021-09-01 08:15:00 | 98            |
| 2021-09-01 08:30:00 | 97            |
| 2021-09-01 08:45:00 | 98            |
| 2021-09-01 09:00:00 | N/A           |
| 2021-09-01 09:15:00 | 96            |
| 2021-09-01 09:30:00 | 94            |
| 2021-09-01 09:45:00 | 93            |
| 2021-09-01 10:00:00 | 90            |

Since we are trying to measure the effect of a drug on something in the body, we don’t want to assume that LOCF or NOCB will apply here, as that could introduce significant error in our analysis. Instead, we could employ BOCF, which could look something like this:

```py
# Isolate the first (baseline) value for our data
baseline = df['concentration'][0]

# Replace missing values with our baseline value
df['concentration'].fillna(value=baseline, inplace=True)
```
Another alternative for single imputation is WOCF, or Worst Observation Carried Forward. With this kind of imputation, we want to assume that the data is the worst possible value. This would be useful if the purpose of our analysis was to record improvement in some value (for example, if we wanted to study if a treatment was helping a particular patient’s condition). By filling in data with the worst value, then we can reduce potentially biased results that didn’t actually happen.

Let’s look at another example dataset. In this dataset, we are tracking a patient’s pain level over the course of a therapy program. The patient rates their pain on a scale of 1 to 10, with 10 being the highest.

|    date    | pain |
|:----------:|:----:|
| 2021-09-01 | 8    |
| 2021-09-02 | 8    |
| 2021-09-03 | 9    |
| 2021-09-04 | 7    |
| 2021-09-05 | N/A  |
| 2021-09-06 | 6    |
| 2021-09-07 | 7    |
| 2021-09-08 | 5    |
| 2021-09-09 | 5    |

This is a great use case for WOCF. Since we are tracking a patient’s pain level, with the goal of reducing that pain level, we would not want to assume that the patient is feeling better than they are, as that could affect their long-term recovery. Thus, we would always want to assume a higher pain level than the reality, so we can heal them more. This would look like the following code block:

```py


# Isolate worst pain value (in this case, the highest)
worst = df['pain'].max()

# Replace all missing values with the worst value
df['pain'].fillna(value=worst, inplace=True)
```

# What are the disadvantages?

Single imputation methods are very useful when we have missing data. By using these methods, we can easily and quickly fill in missing data from contextual information in the dataset. There are, however, some disadvantages to using single imputation methods.

The biggest disadvantage of these methods is the potential for adding bias into a dataset. When we use single imputation, we assume that the data we are using to fill in the blanks is reliable and accurate for that observation. This isn’t always the case, however. Data often will change in unexpected ways. Single imputation will ignore these potential changes and will “smooth” out our data, which could lead to inaccurate results.

In general, single imputation can be an effective technique to handle missing data for our time-series datasets. While it might not be the most sophisticated approach, it can be a useful quick-fix in the right circumstances.

### Coding question
You are presented with this dataset that has two separate values reported over the course of 10 minutes. Use either LOCF or NOCB to fill in the missing value in the value1 column. 

|      timestamp      | value1 | value2 |
|:-------------------:|:------:|:------:|
| 2021-11-11 12:00:00 | 1.0    | 10.0   |
| 2021-11-11 12:01:00 | 1.0    | 10.0   |
| 2021-11-11 12:02:00 | 2.0    | 9.0    |
| 2021-11-11 12:03:00 | 3.0    | 7.0    |
| 2021-11-11 12:04:00 | 4.0    | NaN    |
| 2021-11-11 12:05:00 | 4.0    | 5.0    |
| 2021-11-11 12:06:00 | 4.0    | 5.0    |
| 2021-11-11 12:07:00 | NaN    | 5.0    |
| 2021-11-11 12:08:00 | 6.0    | 5.0    |
| 2021-11-11 12:09:00 | 6.0    | 5.0    |

```py
mport pandas as pd
import numpy as np

d = {'timestamp': ['2021-11-11 12:00:00','2021-11-11 12:01:00','2021-11-11 12:02:00','2021-11-11 12:03:00','2021-11-11 12:04:00',
                    '2021-11-11 12:05:00','2021-11-11 12:06:00','2021-11-11 12:07:00','2021-11-11 12:08:00','2021-11-11 12:09:00'],
    'value1': [1,1,2,3,4,4,4,np.nan,6,6],
    'value2': [10,10,9,7,np.nan,5,5,5,5,5]
    }

df = pd.DataFrame(data=d)

## Fill in the missing data in the value1 column
df['value1'].ffill(axis=0, inplace=True)

print(df)
```


### Coding question
Questions

You are presented with this dataset that has two separate values reported over the course of 10 minutes. Use either LOCF or NOCB to fill in the missing value in the value2 column. 

|      timestamp      | value1 | value2 |
|:-------------------:|:------:|:------:|
| 2021-11-11 12:00:00 | 1.0    | 10.0   |
| 2021-11-11 12:01:00 | 1.0    | 10.0   |
| 2021-11-11 12:02:00 | 2.0    | 9.0    |
| 2021-11-11 12:03:00 | 3.0    | 7.0    |
| 2021-11-11 12:04:00 | 4.0    | NaN    |
| 2021-11-11 12:05:00 | 4.0    | 5.0    |
| 2021-11-11 12:06:00 | 4.0    | 5.0    |
| 2021-11-11 12:07:00 | NaN    | 5.0    |
| 2021-11-11 12:08:00 | 6.0    | 5.0    |
| 2021-11-11 12:09:00 | 6.0    | 5.0    |

```py
import pandas as pd
import numpy as np

d = {'timestamp': ['2021-11-11 12:00:00','2021-11-11 12:01:00','2021-11-11 12:02:00','2021-11-11 12:03:00','2021-11-11 12:04:00',
                    '2021-11-11 12:05:00','2021-11-11 12:06:00','2021-11-11 12:07:00','2021-11-11 12:08:00','2021-11-11 12:09:00'],
    'value1': [1,1,2,3,4,4,4,np.nan,6,6],
    'value2': [10,10,9,7,np.nan,5,5,5,5,5]
    }

df = pd.DataFrame(data=d)

## Fill in the missing data in the 'value2' column
df['value2'].bfill(axis=0, inplace=True)


print(df)
```

