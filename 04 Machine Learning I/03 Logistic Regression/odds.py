import numpy as np
proportion = 0.35

odds = proportion / (1-proportion)
print("odds", odds)

print("log odds: ", np.log(odds))