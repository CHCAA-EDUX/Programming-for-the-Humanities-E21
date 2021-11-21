#!/usr/bin/python3
"""
Sigmoid activation function
    - input: numeric value to pass to activation function
    - usage: python act_sigmoid.py --input 0
"""
import argparse
import numpy as np

def sigmoid(x):
    """Sigmoid activation function: f(x) = 1 / (1 + e^(-x))
    """
    return 1 / (1 + np.exp(-x))

def main():
    ap = argparse.ArgumentParser(description="[Info] sigmoid function for neural network")
    ap.add_argument("-i", "--input", required=True, type=float, help="input value to sigmoid")
    args = vars(ap.parse_args())
    # inference
    x = args["input"]
    y_hat = sigmoid(x)
    print("[INFO] output is {}".format(round(y_hat),3))

if __name__ == '__main__':
    main()
