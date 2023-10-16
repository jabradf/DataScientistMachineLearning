import numpy as np
import noshmishmosh
from scipy.stats import chi2_contingency

allvisitors = noshmishmosh.customer_visits
paying_visitors = noshmishmosh.purchasing_customers

total_visitor_count = len(allvisitors)
paying_visitor_count = len(paying_visitors)
print(paying_visitor_count, total_visitor_count)

baseline_percent = paying_visitor_count/ total_visitor_count * 100
print("baseline percent: ", baseline_percent)

payment_history = noshmishmosh.money_spent
average_payment = np.mean(payment_history)
print("average payment: ", average_payment )

money_needed = 1240
new_customers_needed = np.ceil(money_needed / average_payment)
print("new customers needed: ", new_customers_needed )

percentage_point_increase = new_customers_needed/total_visitor_count*100
print("percentage point increase: ", percentage_point_increase)

# minimum detectable effect/lift
mde = percentage_point_increase/baseline_percent*100
print("MDE: ", mde)

#set sample size to a starter of 10%
sample_size = 490