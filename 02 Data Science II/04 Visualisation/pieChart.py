from matplotlib import pyplot as plt

payment_method_names = ["Card Swipe", "Cash", "Apple Pay", "Other"]
payment_method_freqs = [270, 77, 32, 11]

plt.pie(payment_method_freqs, labels=payment_method_names, autopct='%0.1f%%')
plt.axis('equal')
plt.legend(payment_method_names)
#plt.legend(payment_method_names)

plt.show()

##########################

from matplotlib import pyplot as plt

unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
num_hardest_reported = [1, 3, 10, 15, 1]

#Make your plot here
plt.figure(figsize=(10,8))
plt.pie(num_hardest_reported, labels=unit_topics, autopct='%1d%%')
plt.axis('equal')

plt.title("Hardest Topics")
plt.show()
plt.savefig('my_pie_chart.png')