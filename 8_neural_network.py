import math
import nnfs 
from nnfs.datasets import spiral_data

import numpy as np 

class NeuralLayer:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))
    
    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases 
    
class Activation_Func:
    def relu_activation(self,inputs):
        self.relu_output = np.maximum(0, inputs)
    
    def softmax_activation(self, inputs):
        exp_values = np.exp(inputs - np.max(inputs, axis=1, keepdims=True))
        probabilities = exp_values/ np.sum(exp_values, axis=1, keepdims=True)
        self.softmax_output = probabilities

x, y = spiral_data(samples=100, classes=5)

layer1 = NeuralLayer(
    n_inputs=2, 
    n_neurons=5
)
activation = Activation_Func()

layer2 = NeuralLayer(
    n_inputs=5, 
    n_neurons=5
)

layer1.forward(x)
activation.relu_activation(layer1.output)

layer2.forward(activation.relu_output)
activation.softmax_activation(layer2.output)

print(activation.softmax_output)