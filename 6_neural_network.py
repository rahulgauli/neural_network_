import numpy as np
import nnfs
from nnfs.datasets import spiral_data

nnfs.init()

class Layer_Dense:    
    def __init__(self, n_inputs, n_neurons):
        self.weights =0.10 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))

    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases

    def __repr__(self):
        return f"Layer wt: {str(self.weights)}, biases: {str(self.biases)}"


class Activation_ReLU:
    def forward(self, inputs):
        self.output = np.maximum(0, inputs)


class Activation_Softmax:
    def forward(self, inputs):
        exp_values = np.exp(inputs - np.max(inputs, axis=1, keepdims = True))
        probabilities = exp_values/ np.sum(exp_values, axis=1, keepdims=True)
        self.output = probabilities

x, y = spiral_data(samples=100, classes=3)
dense1 = Layer_Dense(2,90)
activation1 = Activation_ReLU()

dense2 = Layer_Dense(90, 3)
activation2 = Activation_Softmax()

dense3 = Layer_Dense(3, 3)


dense1.forward(x)
activation1.forward(dense1.output)

dense2.forward(activation1.output)
activation1.forward(dense2.output)

dense3.forward(activation1.output)
activation2.forward(dense3.output)


print(activation2.output)