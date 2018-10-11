"""
    This pre-code is a nice starting point, but you can
    change it to fit your needs.
"""
import numpy as np
import random as rd
from perceptron import Perceptron

class mlp:
    def __init__(self, inputs, targets, nhidden, bias_value=-1):
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
            self.hidden.append(Perceptron(self.no_inputs, self.beta, bias_value))

        #Initiate output layer
        self.output = []
        for i in range(self.no_outputs):
            self.output.append(Perceptron(self.no_hidden, self.beta, bias_value))


    # You should add your own methods as well!

    def earlystopping(self, inputs, targets, valid, valid_targets):
        copy_hidden = []
        copy_output = []
        epoch = 0
        old_accuracy = 0
        self.train(inputs, targets)
        new_accuracy = self.validation(valid, valid_targets)
        for i in range(75):
            while new_accuracy >= old_accuracy:
                print("Epoch: " , epoch)
                copy_hidden = self.hidden.copy()
                copy_output = self.output.copy()
                old_accuracy = new_accuracy
                self.train(inputs, targets)
                new_accuracy = self.validation(valid, valid_targets)
                epoch += 1
            self.train(inputs, targets)
            new_accuracy = self.validation(valid, valid_targets)
            if new_accuracy > old_accuracy:
                i = 0

        self.hidden = copy_hidden.copy()
        self.output = copy_output.copy()


    def train(self, inputs, targets, iterations=75):
        for i in range(iterations):
            index = rd.randint(0, len(self.inputs) - 1)
            data = inputs[index]
            target = targets[index]
            result = self.forward(data)
            self.backward(result, target, data)


    def validation(self, valid, valid_targets):
        total_tests = len(valid)
        correct = 0
        for inputs, targets in zip(valid, valid_targets):
            result = self.forward(inputs)
            if(self.check_correct(result, targets)):
                correct += 1

        accuracy = correct / total_tests
        return accuracy

    def check_correct(self, result, target):
        right_index = 0
        for i in range(len(target)):
            if target[i] == 1:
                right_index = i

        result_index = 0
        max_value = 0
        for i in range(len(result)):
            current = result[i]
            if current > max_value:
                max_value = result[i]
                result_index = i

        #print("Result: ", result_index, " right", right_index)


        if result_index != right_index:
            return False

        return True

    def forward(self, data):
        hidden_outputs = []
        for node in self.hidden:
            hidden_outputs.append(node.calc_out(data))

        result = []
        for node in self.output:
            result.append(node.calc_out(hidden_outputs))

        return result


    def backward(self, result, target, input_values):
        for count, output_node in enumerate(self.output, 0):
            output_node.error_o(target[count])

        for count, hidden_node in enumerate(self.hidden, 0):
            errors = []
            weights = []
            for output_node in self.output:
                errors.append(output_node.error)
                weights.append(output_node.weights[count])
            hidden_node.error_h(errors, weights)

        for node in self.output:
            for count, hidden_node in enumerate(self.hidden, 0):
                node.update_weight(self.eta, hidden_node.output, count)
            node.update_bias(self.eta)

        for node in self.hidden:
            for count, value in enumerate(input_values, 0):
                node.update_weight(self.eta, value, count)
            node.update_bias(self.eta)

    def confusion(self, inputs, targets):
        print('To be implemented')