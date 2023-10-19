#1. Information gain at a pure node (i.e., node with no more branches!)
r = 0.5 #ratio of new split, could be anything
gini_pure_node = 0
gini_info_gain = r*gini_pure_node  + (1-r)*gini_pure_node 
print(f'Gini information gain pure node split safety_low >= .5 : {gini_info_gain}')

#2. Information gain at the 'persons_2' split
r_persons_2 = 604/912 #read ratio of the split from the tree!
gini_left_split = 0.434
gini_right_split = 0
gini_info_gain_persons_2 = r_persons_2*gini_left_split + r_persons_2*gini_right_split
print(f'Gini information gain node persons_2 : {gini_info_gain_persons_2}')

# quiz, currently not working as anwser is 0.125!
# (node info gini = 0.5, samples = 39, value = [19,20], class=quit)
samplesleft = 16
samplesright = 23
totalsamples = 39
leftRatio = samplesleft/totalsamples
rightRatio = samplesright/totalsamples
ginileft = 0.305
giniright = 0.423
initial_purity = 0.5
quiz_info_gain = leftRatio * ginileft + rightRatio * giniright
print(quiz_info_gain)