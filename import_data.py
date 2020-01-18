import pandas as pd
import numpy as np
import statsmodels
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
                 'Neighbour': 160 * 10 ** -3}

powerCO2Emissions = {'Nuclear': 68,  # g of CO2 emissions per kWH
                 'Solar': 481,
                 'Wind': 133,
                 'Hydro': 57,
                 'Gas': 140,
                 'Biofuel': 131,
                 'Neighbour': 160}