import numpy as np

def onestep(x):
    b = 5
    if x >= b:
        return 1
    else:
        return 0

class Neuron:
    def __init__(self, w):
        self.w = w

    def y(self, x):
        s = np.dot(self.w, x)
        return onestep(s)

Xi = np.array([0, 0, 1, 1])
Wi = np.array([5, 4, 3, 1])
n = Neuron(Wi)
print('Y =', n.y(Xi))
