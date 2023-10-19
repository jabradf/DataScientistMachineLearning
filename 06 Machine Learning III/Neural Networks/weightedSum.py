class Perceptron:
  def __init__(self, num_inputs=2, weights=[2,1]):
    self.num_inputs = num_inputs
    self.weights = weights
    
  def weighted_sum(self, inputs):
    # create variable to store weighted sum
    weighted_sum=0
    for i in range(self.num_inputs):
      weighted_sum += self.weights[i] * inputs[i]
    
    return weighted_sum
    
      
cool_perceptron = Perceptron()
res = cool_perceptron.weighted_sum([24, 55])
print(res)
