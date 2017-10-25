class CEAlgorithm:
    def __init__(self):
        self.attributes = {}
        self.all_general = []
        self.general = []
        self.specific = []
        self.training_examples = []

    def set_attributes(self, key, value):
        self.attributes[key] = value

    def set_training_example(self, examples):
        self.training_examples = examples

    def get_output(self):
        self.train_examples()

    def train_examples(self):
        count = len(self.training_examples[0])
        self.init_max_general(count - 1)
        self.init_max_specific(count - 1)
        for i in self.training_examples:
            if i[-1] == "yes":
                self.more_general(i[:-1])
            elif i[-1] == "no":
                self.more_specific(i[:-1])

    def init_max_general(self, count):
        for i in range(count):
            self.general.append("?")

    def init_max_specific(self, count):
        for i in range(count):
            self.specific.append('0')

    def more_general(self, example):
        key = 0
        for i in example:
            if self.specific[key] == '0':
                self.specific[key] = i
            elif self.specific[key] == i:
                pass
            else:
                if len(self.attributes[list(self.attributes.keys())[key]]) == 2:
                    self.specific[key] = '?'
                else:
                    self.specific[key] = [self.specific[key], i]
                    if self.specific[key] == self.attributes[list(self.attributes.keys())[key]]:
                        self.specific[key] = '?'
            key += 1
        if len(self.all_general) > 0:
            self.check_consistency()

    def more_specific(self, example):
        key = 0
        if len(self.all_general) == 0:
            for i in example:
                for j in self.attributes[list(self.attributes.keys())[key]]:
                    if (j in self.specific[key]) and (j != i):
                        general = self.general[:]
                        general[key] = j
                        if general not in self.all_general:
                            self.all_general.append(general)
                key += 1
        self.check_consistency()

    def check_consistency(self):
        count = 0
        for k in self.all_general:
            for x in range(len(k)):
                if self.specific[x] == '?' and k[x] != '?':
                    del self.all_general[count]
            count += 1


examples = [['sunny', 'warm', 'normal', 'strong', 'warm', 'same', 'yes'],
            ['sunny', 'warm', 'high', 'strong', 'warm', 'same', 'yes'],
            ['rainy', 'cool', 'high', 'strong', 'warm', 'change', 'no'],
            ['sunny', 'warm', 'high', 'strong', 'cool', 'change', 'yes']]


ce = CEAlgorithm()

ce.set_attributes('sky', ['sunny', 'cloudy', 'rainy'])
ce.set_attributes('temperature', ['cool', 'warm'])
ce.set_attributes('humidity', ['normal', 'high'])
ce.set_attributes('wind', ['light', 'strong'])
ce.set_attributes('water', ['warm', 'cold'])
ce.set_attributes('forecast', ['same', 'change'])
ce.set_attributes('water', ['warm', 'cold'])

ce.set_training_example(examples)

ce.get_output()
print(ce.specific, ce.all_general)

