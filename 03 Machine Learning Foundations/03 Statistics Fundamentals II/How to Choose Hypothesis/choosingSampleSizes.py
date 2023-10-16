# calculate baseline:
baseline = 10
print("baseline: ", baseline)

# calculate MDE:
MDE = (new - baseline) / baseline * 100
print("Minimum Detectable Effect: ", MDE)

# calculate significance threshold:
sig_threshold = 5	# for 5%
print("significance threshold: ", sig_threshold)

# calculate total sample size: 
samp_size= 2060	# look up how to do ab sampe size calculation in python!!
print("sample size: ", samp_size)

'''
number_of_site_visitors = 2000.0
number_of_converted_visitors = 1300.0

# calculate baseline_rate and print it out:
baseline_rate = number_of_converted_visitors/number_of_site_visitors*100


baseline = 8
new = 12
mde = (new - baseline) / baseline * 100
print(mde) #output: 33.0



'''