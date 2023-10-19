# the lower the number, the more pure the data is!
p1 = 412/1382
p2 = 970/1382

gini_root = 1 - (p1**2 + (1-p1)**2)
print(f'Gini impurity root node : {gini_root}')

p1 = 353/449
p2 = 96/449
gini_bottom_left = 1 - (p1**2 + (1-p1)**2)
print(f'Gini impurity bottom left node : {gini_bottom_left}')


p1_2 = 235/674
p2_2 = 439/674
gini_root2 = 1 - (p1_2**2 + (1-p1_2)**2)

print("quiz gini:",gini_root2)

def ginifn(p1):
    return 1 - (p1**2 + (1-p1)**2)

prob1 = 80/100
prob2 = 50/100
prob3 = 90/100
prob4 = 95/100

print(ginifn(prob1))
print(ginifn(prob2))
print(ginifn(prob3))
print(ginifn(prob4))