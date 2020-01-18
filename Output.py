class Output:
    def __init__(self, array):
        if array is None:
            array = [0 for i in range(19)]
        self.time = array[1]
        self.supplied = array[2]
        self.sources = {}
        self.sources["solar"] = array[3]
        self.sources["nuclear"] = array[4]
        self.sources["wind"] = array[5]
        self.sources["hydro"] = array[6]
        self.sources["gas"] = array[7]
        self.sources["biofuel"] = array[8]
        self.sources["neighbor"] = array[9]
        self.diff = array[10]
        self.green = array[11]
        self.bought = array[12]
        self.sold = array[13]
        self.co2 = array[14]
        self.price = array[15]
        self.cost = array[16]
        self.margin = array[17] # called "Diff" on sample, but that name is used above
    def to_array(self):
        array = [0 for i in range(19)]
        array[0] = 2
        array[1] = self.time
        array[2] = self.supplied
        array[3] = self.sources["solar"]
        array[4] = self.sources["nuclear"]
        array[5] = self.sources["wind"]
        array[6] = self.sources["hydro"]
        array[7] = self.sources["gas"]
        array[8] = self.sources["biofuel"]
        array[9] = self.sources["neighbor"]
        array[10] = self.diff
        array[11] = self.green
        array[12] = self.bought
        array[13] = self.sold
        array[14] = self.co2
        array[15] = self.price
        array[16] = self.cost
        array[17] = self.margin
        array[18] = -1
        return array