import numpy as np

def sigmoid(x):
    return 1/(1+np.exp(-x))

class Neuron:
    def __init__(self, w):
        self.w = w

    def y(self, x):
        s = np.dot(self.w, x)
        return sigmoid(s)

Xi = np.array([0, 0, 0, 0])
Wi = np.array([5, 4, 3, 1])
n = Neuron(Wi)
print('Y =', n.y(Xi))
