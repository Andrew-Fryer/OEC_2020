# Make objects to hold input data rows

class Input:
    def __init__(self, array):
        self.time = array[1]
        self.demands = array[2]
        self.sources = {}
        self.sources["solar"] = array[3]
        self.sources["nuclear"] = array[4]
        self.sources["wind"] = array[5]
        self.sources["hydro"] = array[6]
        self.sources["gas"] = array[7]
        self.sources["biofuel"] = array[8]
        self.sources["neighbor"] = array[9]
        self.h0 = array[10]
        self.h1 = array[11]
        self.h2 = array[12]
        self.h3 = array[13]
        self.h4 = array[14]
        self.solar_coef = array[15]
        self.wind_coef = array[16]
        self.hydro_coef = array[17]
        self.neighbor_power = array[18]
        self.neighbor_price = array[19]
        self.last_week = [array[20], array[21], array[22], array[23], array[24], array[25]]