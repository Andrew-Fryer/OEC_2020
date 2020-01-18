import helpers as helper
import re

class Output:
    def __init__(self, input):
        self.sources = {}
    def to_array(self, input):
        array = [0 for i in range(19)]
        array[0] = 2
        array[1] = input.time
        supplied = 0
        for source in list(self.sources.items()):
            supplied += source[1]
        array[2] = supplied
        array[3] = self.sources["solar"]
        array[4] = self.sources["nuclear"]
        array[5] = self.sources["wind"]
        array[6] = self.sources["hydro"]
        array[7] = self.sources["gas"]
        array[8] = self.sources["biofuel"]
        array[9] = self.sources["neighbor"]
        array[10] = supplied - input.demands
        green = sum([self.sources["solar"], self.sources["wind"], self.sources["hydro"], self.sources["biofuel"]])
        array[11] = green
        array[12] = max(self.sources["neighbor"], 0)
        array[13] = min(self.sources["neighbor"], 0)
        array[14] = helper.co2(self.sources)
        last_index = re.match("([0-9]*):", input.time).lastindex # regex to parse time
        price = helper.rate(helper.isSummer(input.last_week), int(input.time[:last_index])) * supplied
        array[15] = price
        cost = helper.cost(self.sources)
        array[16] = cost
        array[17] = (price - cost) * supplied
        array[18] = -1
        return array