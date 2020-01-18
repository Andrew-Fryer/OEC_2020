# Helper functions

# helper to calculate cost:
powerCost = {'Nuclear': 68,  # $ per MWH
                 'Solar': 481,
                 'Wind': 133,
                 'Hydro': 57,
                 'Gas': 140,
                 'Biofuel': 131,
                 'Neighbour': 160
             }
def cost(sources):
    temp = sources["nuclear"] * powerCost["Nuclear"]
    + sources["solar"] * powerCost["Solar"]
    + sources["wind"] * powerCost["Wind"]
    + sources["hydro"] * powerCost["Hydro"]
    + sources["gas"] * powerCost["Gas"]
    + sources["biofuel"] * powerCost["Biofuel"]
    + sources["neighbor"] * powerCost["Neighbour"]
    
    return temp

# helper to calculate co2 emisssions:
powerCO2Emissions = {'Nuclear': 68 * 10 ** 3,  # g of CO2 emissions per MWH
                 'Solar': 481 * 10 ** 3,
                 'Wind': 133 * 10 ** 3,
                 'Hydro': 57 * 10 ** 3,
                 'Gas': 140 * 10 ** 3,
                 'Biofuel': 131 * 10 ** 3,
                 'Neighbour': 160 * 10 ** 3
                     }

renewableAverages = {"Solar": 85.62 * 10 ** 3, # average power output for each renewable energy source.
                     'Wind': 776.26 * 10 ** 3, # Multiply this # by coeffiecient to compute expected energy production.
                     "Hydro": 3675.79 * 10 ** 3
                     }
def co2(sources):
    return (sources["nuclear"] * powerCO2Emissions["Nuclear"]
    + sources["solar"] * powerCO2Emissions["Solar"]
    + sources["wind"] * powerCO2Emissions["Wind"]
    + sources["hydro"] * powerCO2Emissions["Hydro"]
    + sources["gas"] * powerCO2Emissions["Gas"]
    + sources["biofuel"] * powerCO2Emissions["Biofuel"]
    + sources["neighbor"] * powerCO2Emissions["Neighbour"])

# helper to determine season from temperatures in the past week
def isSummer(last_week):
    avg_temp = sum(last_week) / len(last_week)
    return avg_temp > 10

# helper to calculate power pricing rate:
def rate(isSummer: bool, hour: int): # return correct rate for price of a kilowatt based on the current hydro rate
    if hour < 0 or hour > 23:
        raise ValueError
    elif hour < 7 or hour > 18:
        return 6.5 * 10 ** 1 #  dollars per MWH
    if isSummer:
        if hour < 11 or hour > 16:
            return 9.4  * 10 ** 1  # dollars per MWH
        else:
            return 13.4  * 10 ** 1 # dollars per MWH
    else:
        if hour < 11 or hour > 16:
            return 13.4  * 10 ** 1  # dollars per MWH
        else:
            return 9.4  * 10 ** 1 # dollars per MWH
