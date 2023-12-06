class n():
    def __init__(self):
        self.weight = 56.97
        #0.621370900000024
        #0.6209999900000018
        self.last_error = 1
        self.smoothing = 0.0001
#0.6209999900000018 0.6209999900000035
    def get_last_error(self):
        return self.last_error

    def get_smoothing(self):
        return self.smoothing

    def get_weight(self):
        return self.weight


    def process_input_data(self, input_data):
        return input_data * self.weight

    def train(self, input, excpectedResult):
        result_now = input * self.weight
        self.last_error = excpectedResult - result_now
        correction = self.last_error / result_now
        correction = correction * self.smoothing
        self.weight += correction

    def check_training(self):
        if (self.last_error > self.smoothing or self.last_error < - self.smoothing):
            return True
        else:
            return False


neuron = n()
#input_data = input("Введите: ")
input_data = float(1)
excpectedResult = 
#
i = 1
while (neuron.check_training()):
    neuron.train(input_data, excpectedResult)
    if i % 10000 == 0:
        print(str(i))
        pass
    i += 1
print('Successful')
print(neuron.get_weight())
print(neuron.process_input_data(input_data))



#print (neuron.process_input_data(input_data))
#




































