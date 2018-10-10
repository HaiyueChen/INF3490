"""
    This pre-code is a nice starting point, but you can
    change it to fit your needs.
"""
import numpy as np
import random as rd

class mlp:
    def __init__(self, inputs, targets, nhidden):
        self.beta = 1
        self.eta = 0.1
        self.momentum = 0.0
        self.no_hidden = nhidden

        self.inputs = inputs
        self.no_inputs = len(inputs[0])
        self.targets = targets
        self.no_outputs = len(targets[0])

        #Initiate hidden layer
        self.hidden = []
        for i in range(self.no_hidden):
            self.hidden.append(Perceptron(self.no_inputs, self.beta))

        #Initiate output layer
        self.output = []
        for i in range(self.no_outputs):
            self.output.append(Perceptron(self.no_hidden, self.beta))


        print('To be implemented')

    # You should add your own methods as well!

    def earlystopping(self, inputs, targets, valid, validtargets):
        print('To be implemented')

    def train(self, inputs, targets, iterations=100):
        for i in range(iterations):
            index = rd.randint(0, len(self.inputs) - 1)
            data = inputs[index]
            target = targets[index]
            result = self.forward(data)
            self.backward(result, target)

    def forward(self, data):
        hidden_outputs = []
        for node in self.hidden:
            hidden_outputs.append(node.calc_out(data))

        result = []
        for node in self.output:
            result.append(node.calc_out(hidden_outputs))

        return result


    def backward(self, result, target):
        for count, output_node in enumerate(self.output, 0):
            output_node.error_o(target[count])

        for count, hidden_node in enumerate(self.hidden, 0):
            errors = []
            weights = []
            for output_node in self.output:
                error.append(output_node.error)
                weights.append(output_node.weight[count])
            hidden_node.error_h(errors, weights)

        for node in output_node:
            for count, hidden_node in enumerate(self.hidden, 0):
                node.update_weight(self.eta, hidden_node.output, count)


    def confusion(self, inputs, targets):
        print('To be implemented')