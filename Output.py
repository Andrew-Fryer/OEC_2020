class Output:
    def __init__(self, array):
        self.time = array[1]
        self.supplied = array[2]
        self.solar = array[3]
        self.nuclear = array[4]
        self.wind = array[5]
        self.hydro = array[6]
        self.gas = array[7]
        self.biofeul = array[8]
        self.neighbor = array[9]
        self.diff = array[10]
        self.green = array[11]
        self.bought = array[12]
        self.sold = array[13]
        self.co2 = array[14]
        self.price = array[15]
        self.cost = array[16]
        self.margin = array[17] # called "Diff" on sample, but that name is used above