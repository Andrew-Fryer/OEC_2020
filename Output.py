class Output:
    def __init__(self, array):
        if array is None:
            array = [0 for i in range(19)]
        self.time = array[1]
        self.supplied = array[2]
        self.solar = array[3]
        self.nuclear = array[4]
        self.wind = array[5]
        self.hydro = array[6]
        self.gas = array[7]
        self.biofuel = array[8]
        self.neighbor = array[9]
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
        array[3] = self.solar
        array[4] = self.nuclear
        array[5] = self.wind
        array[6] = self.hydro
        array[7] = self.gas
        array[8] = self.biofuel
        array[9] = self.neighbor
        array[10] = self.diff
        array[11] = self.green
        array[12] = self.bought
        array[13] = self.sold
        array[14] = self.co2
        array[15] = self.price
        array[16] = self.cost
        array[17] = self.margin
        array[18] = -1