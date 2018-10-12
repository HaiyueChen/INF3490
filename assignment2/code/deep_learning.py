"""
    This pre-code is a nice starting point, but you can
    change it to fit your needs.
"""
import numpy as np
import random as rd
from perceptron import Perceptron


class deep_learning:
    def __init__(self, inputs, targets, nhidden_1, nhidden_2, bias_value=-1):
        self.beta = 1
        self.eta = 0.1
        self.momentum = 0.0
        self.no_hidden_1 = nhidden_1
        self.no_hidden_2 = nhidden_2

        self.inputs = inputs
        self.no_inputs = len(inputs[0])
        self.targets = targets
        self.no_outputs = len(targets[0])

        #Initiate hidden layer 1
        self.hidden_1 = []
        for i in range(self.no_hidden_1):
            self.hidden_1.append(
                Perceptron(self.no_inputs, self.beta, bias_value)
                )

        #Initiate hidden layer 2
        self.hidden_2 = []
        for i in range(self.no_hidden_2):
            self.hidden_2.append(
                Perceptron(self.no_hidden_1, self.beta, bias_value)
            )

        #Initiate output layer
        self.output = []
        for i in range(self.no_outputs):
            self.output.append(
                Perceptron(self.no_hidden_2, self.beta, bias_value)
                )

    # You should add your own methods as well!

    def earlystopping(self, inputs, targets, valid, valid_targets):
        copy_hidden_1 = []
        copy_hidden_2 = []
        copy_output = []
        epoch = 0
        old_accuracy = 0
        self.train(inputs, targets)
        new_accuracy = self.validation(valid, valid_targets)
        for i in range(75):
            while new_accuracy >= old_accuracy:
                print("Epoch: ", epoch)
                copy_hidden_1 = self.hidden_1.copy()
                copy_hidden_2 = self.hidden_2.copy()
                copy_output = self.output.copy()
                old_accuracy = new_accuracy
                self.train(inputs, targets)
                new_accuracy = self.validation(valid, valid_targets)
                epoch += 1
            self.train(inputs, targets)
            new_accuracy = self.validation(valid, valid_targets)
            if new_accuracy > old_accuracy:
                i = 0

        self.hidden_1 = copy_hidden_1.copy()
        self.hidden_2 = copy_hidden_2.copy()
        self.output = copy_output.copy()

    def train(self, inputs, targets, iterations=200):
        for i in range(iterations):
            index = rd.randint(0, len(self.inputs) - 1)
            data = inputs[index]
            target = targets[index]
            result = self.forward(data)
            print(result)
            self.backward(result, target, data)

    def validation(self, valid, valid_targets):
        total_tests = len(valid)
        correct = 0
        for inputs, targets in zip(valid, valid_targets):
            result = self.forward(inputs)
            if (self.check_correct(result, targets)):
                correct += 1

        accuracy = correct / total_tests
        return accuracy

    def check_correct(self, result, target):
        right_index = np.argmax(target)
        result_index = np.argmax(result)

        return result_index == right_index

    def forward(self, data):
        hidden_outputs_1 = []
        for node in self.hidden_1:
            hidden_outputs_1.append(node.calc_out(data))

        hidden_outputs_2 = []
        for node in self.hidden_2:
            hidden_outputs_2.append(node.calc_out(hidden_outputs_1))

        result = []
        for node in self.output:
            result.append(node.calc_out(hidden_outputs_2))

        return result

    def backward(self, result, target, input_values):
        #set error for output nodes
        for count, output_node in enumerate(self.output, 0):
            output_node.error_o(target[count])

        #set error for hidden layer 2
        for count, hidden_node_2 in enumerate(self.hidden_2, 0):
            errors = []
            weights = []
            for output_node in self.output:
                errors.append(output_node.error)
                weights.append(output_node.weights[count])
            hidden_node_2.error_h(errors, weights)
        
        #set error for hidden layer 1
        for count, hidden_node_1 in enumerate(self.hidden_1, 0):
            errors = []
            weights = []
            for hidden_node_2 in self.hidden_2:
                errors.append(hidden_node_2.error)
                weights.append(hidden_node_2.weights[count])
            hidden_node_1.error_h(errors, weights)


        #update weights for output nodes
        for node in self.output:
            for count, hidden_node_2 in enumerate(self.hidden_2, 0):
                node.update_weight(self.eta, hidden_node_1.output, count)
            node.update_bias(self.eta)

        #update weights for hidden layer 2
        for node in self.hidden_2:
            for count, hidden_node_1 in enumerate(self.hidden_1, 0):
                node.update_weight(self.eta, hidden_node_1.output, count)
            node.update_bias(self.eta)

        #update weights for hidden layer 1
        for node in self.hidden_1:
            for count, value in enumerate(input_values, 0):
                node.update_weight(self.eta, value, count)
            node.update_bias(self.eta)

    def confusion(self, inputs, targets):
        matrix = []
        for i in range(len(targets[0])):
            matrix.append([0] * len(targets[0]))

        result = []
        for element, target in zip(inputs, targets):
            result = self.forward(element)
            result_index = np.argmax(result)
            target_index = np.argmax(target)
            matrix[target_index][result_index] += 1

        print(np.array(matrix))