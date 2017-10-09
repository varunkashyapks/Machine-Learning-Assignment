
import math
import copy

# Building the ID3 Decision Tree Algorithm
class DecisionTree:
    def __init__(self):
        self.__structure = None
        self.__attributes = None

    def __entropy(self, attributes, target_attribute, data):
        entropy = 0.0
        freq = {}
        try:
            i = attributes.index(target_attribute)
        except ValueError:
            raise DecisionTreeException(0)
        for individual in data:
            if individual[i] in freq:
                freq[individual[i]] += 1
            else:
                freq[individual[i]] = 1
        for key in freq:
            p = float(freq[key] / len(data))
            if p != 0:
                entropy += -p * math.log2(p)
            else:
                entropy += 0
        return entropy

    def ___choose_attribute(self, attributes, target_attribute, data):
        ret = None
        min_conditional_entropy = None
        if self.__entropy(attributes, target_attribute, data) == 0:
            return ret
        for i in range(len(attributes)):
            if attributes[i] == target_attribute or self.__entropy(attributes, attributes[i], data) == 0:
                continue
            conditional__entropy = 0
            data_seperation = {}
            for individual in data:
                if individual[i] in data_seperation:
                    data_seperation[individual[i]] += [individual]
                else:
                    data_seperation[individual[i]] = [individual]
            for key in data_seperation:
                conditional__entropy += len(data_seperation[key]) / float(len(data)) * self.__entropy(attributes, target_attribute, data_seperation[key])
            if min_conditional_entropy is None:
                min_conditional_entropy = conditional__entropy
                ret = attributes[i]
            elif conditional__entropy < min_conditional_entropy:
                min_conditional_entropy = conditional__entropy
                ret = attributes[i]
            return ret

    def generate(self, Data, Attributes, TargetAttribute):
        try:
            i_target = Attributes.index(TargetAttribute)
        except ValueError:
            raise DecisionTreeException(0)
        if len(Data) == 0:
            return
        self.__structure = [None, {}]  # Structure has to be mutable object
        self.__attributes = Attributes
        open_tab = [[self.__structure,Data]]
        while open_tab != []:
            front = open_tab.pop(0)
            best_attribute = self.___choose_attribute(Attributes, TargetAttribute, front[1])
            if best_attribute is not None:
                front[0][0] = best_attribute
                i = Attributes.index(best_attribute)
                open_tab_increment = []
                data_seperation = {}
                for individual in front[1]:
                    if individual[i] in data_seperation:
                        data_seperation[individual[i]].append(individual)
                    else:
                        data_seperation[individual[i]] = [individual]
                for key in data_seperation:
                    front[0][1][key] = [None, {}]
                    open_tab_increment.append([front[0][1][key], data_seperation[key]])
                open_tab += open_tab_increment
            else:
                front[0][1] = []
                freq = {}
                for individual in front[1]:
                    if individual[i_target] in freq:
                        freq[individual[i_target]] += 1
                    else:
                        freq[individual[i_target]] = 1
                for key in freq:
                    front[0][1].append((key, float(freq[key] / len(front[1]))))

    def predict_prob(self, data):
        iterator = self.__structure
        while iterator[0] is not None:
            i = self.__attributes.index(iterator[0])
            try:
                iterator = iterator[1][data[i]]
            except KeyError:
                raise DecisionTreeException(1)
        ret = copy.deepcopy(iterator[1])
        return ret

    def predict(self, data):
        result_list = self.predict_prob(data)
        return list(sorted(result_list, key=lambda x: x[1], reverse=True))[0][0]

    def __for_the_same(self, attributes, target_attribute, data):
        try:
            i = attributes.index(target_attribute)
        except ValueError:
            raise DecisionTreeException(0)
        class_0 = data[0][i]
        for individual in data:
            if individual[i] != class_0:
                return False
        return True

    def __repr__(self):
        raise NotImplementedError("Implement")


class DecisionTreeException(Exception):
    Exception_Dictionary = {0: "Invalid Target Attribute", 1: "Unpredictable Data"}

    def __init__(self, error_code):
        self.__ErrorCode = error_code

    def __repr__(self):
        return DecisionTreeException.Exception_Dictionary[self.__ErrorCode]
if __name__ == "__main__":
    tree = DecisionTree()
