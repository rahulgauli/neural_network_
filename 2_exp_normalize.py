import numpy as np 
layer_outputs = [[4.8, 1.21, 2.385],
                 [1,4,6],
                 [0.2,.6, 1.7]
                 ]
exp_values = np.exp(layer_outputs)
norm_values =  exp_values / np.sum(exp_values, axis=1, keepdims=True)

print(norm_values)   

#can be done in a batch 