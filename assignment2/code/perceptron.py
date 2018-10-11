import random as rd
from math import exp

class Perceptron:

    def __init__(self, no_inputs, beta, bias_value, is_output=False):
        self.is_output = is_output
        self.weights = []
        self.bias_value = bias_value
        self.beta = beta
        for i in range(no_inputs + 1):
            self.weights.append(rd.uniform(-1, 1))

        self.output = None
        self.error = None

    def calc_out(self, data):
        if len(data) + 1 == len(self.weights):
            weighted_sum = 0
            for (index, value) in enumerate(data):
                weighted_sum += self.weights[index] * value

            weighted_sum += self.bias_value * self.weights[-1]

            self.output = self.sigmoid(weighted_sum)
            return self.output

        else:
            raise ValueError

    def update_weight(self, eta, z, index):
        self.weights[index] -= self.error * eta * z

    def update_bias(self, eta):
        self.weights[-1] -= self.error * eta * self.bias_value

    def error_h(self, errors, weights):
        sigma_sum = 0
        for (err, weight) in zip(errors, weights):
            sigma_sum += err * weight

        self.error = self.delta_sigmoid(self.output) * sigma_sum


    def error_o(self, target):
        self.error = self.output - target


    def sigmoid(self, x):
        if x > 100:
            x = 100
        elif x < -100:
            x = -100

        return (1 / (1 + exp(-x * self.beta)))

    def delta_sigmoid(self, x):
        if x > 100:
            x = 100
        elif x < -100:
            x = -100

        return (self.sigmoid(x) * (1 - self.sigmoid(x)))


if __name__ == "__main__":
    test = Perceptron(10)
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(test.compute(data))
