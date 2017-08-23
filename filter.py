from collections import deque
import __conf__


class Filter:
    def __init__(self, weights, num_of_fields):
        self.q = deque([[0 for _ in range(num_of_fields)] for _ in range(len(weights))])
        self.weights = weights
        self.num_of_fields = num_of_fields

    def get(self, new_values):
        self.q.popleft()
        self.q.append(new_values)
        return self.calculate()

    def calculate(self):
        result = []
        for i in range(self.num_of_fields):
            vsota = sum([element[i]*self.weights[j] for j, element in enumerate(self.q)])
            result.append(vsota / sum(self.weights))
        return result
        # return [sum(elements[i] * self.weights[j] for j, elements in enumerate(self.q)) / sum(self.weights) / sum(self.weights) for i in range(len(self.weights))]
        # return sum(tupl[0]*self.weights[i] for i, tupl in enumerate(self.q)) / sum(self.weights), sum(tupl[2]*__conf__.position_gain*self.weights[i] for i, tupl in enumerate(self.q)) / sum(self.weights)

    @staticmethod
    def r_to_w(r):
        if r == 0: return 0
        r = float(r) * __conf__.meter_to_pixel_ratio  # convert to meters
        return __conf__.v / r
