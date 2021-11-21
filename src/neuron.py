#!/usr/bin/python3
"""
Simple artificial neuron with 2d input
    - input two numerical values separated by ","
    - usage: python neuron.py --input 1,0
"""
import argparse
import numpy as np

def sigmoid(x):
    """Sigmoid activation function: f(x) = 1 / (1 + e^(-x))
    """
    return 1 / (1 + np.exp(-x))


class Neuron:
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias

    def feedforward(self, inputs):
        """ Weight inputs, add bias, then use the activation function
        """
        total = np.dot(self.weights, inputs) + self.bias

        return sigmoid(total)


def main():
    ap = argparse.ArgumentParser(description="[Info] neuron with two inputs")
    ap.add_argument("-i", "--input", required=True, type=str, help="2d input array to neuron")
    ap.add_argument("-b", "--bias", required=False, type=int, default=2, help="integer bias")
    
    args = vars(ap.parse_args())
    # parameters
    x = np.array([float(i) for i in args["input"].split(",")])
    w = np.array([0, 1])
    b = args["bias"]
    # instance
    n = Neuron(w, b)
    # inference
    y_hat = n.feedforward(x)
    print("[INFO] output is {}".format(round(y_hat, 3)))
    # decision
    if y_hat > .5:
        print("[INFO] it is a dog")
    else:
        print("[INFO] it is a cat")


if __name__ == '__main__':
    main()
