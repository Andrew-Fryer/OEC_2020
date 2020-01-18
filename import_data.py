import pandas as pd
import numpy as np
import xlrd


input1 = pd.read_excel('given-files/inputFile1.xlsx')
input2 = pd.read_excel('given-files/inputFile2.xlsx')
input3 = pd.read_excel('given-files/inputFile3.xlsx')

powerCost = {'Nuclear': 68 * 10 ** -3,  # $ per kWH
                 'Solar': 481 * 10 ** -3,
                 'Wind': 133 * 10 ** -3,
                 'Hydro': 57 * 10 ** -3,
                 'Gas': 140 * 10 ** -3,
                 'Biofuel': 131 * 10 ** -3,
                 'Neighbour': 160 * 10 ** -3
             }

powerCO2Emissions = {'Nuclear': 68,  # g of CO2 emissions per kWH
                 'Solar': 481,
                 'Wind': 133,
                 'Hydro': 57,
                 'Gas': 140,
                 'Biofuel': 131,
                 'Neighbour': 160
                     }

renewableAverages = {"Solar": 85.62 * 10 ** 3, # average power output for each renewable energy source.
                     'Wind': 776.26 * 10 ** 3, # Multiply this # by coeffiecient to compute expected energy production.
                     "Hydro": 3675.79 * 10 ** 3
                     }

def rate(isSummer: bool, hour: int): # return correct rate for price of a kilowatt based on the current hydro rate
    if hour < 0 or hour > 23:
        raise ValueError
    elif hour < 7 or hour > 18:
        return 6.5 * 10 ** -2 #  dollars per kWH
    if isSummer:
        if hour < 11 or hour > 16:
            return 9.4  * 10 ** -2  # dollars per kWH
        else:
            return 13.4  * 10 ** -2 # dollars per kWH
    else:
        if hour < 11 or hour > 16:
            return 13.4  * 10 ** -2  # dollars per kWH
        else:
            return 9.4  * 10 ** -2 # dollars per kWH



