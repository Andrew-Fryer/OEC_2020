import Output as output
import Input as input
import pandas as pd

data = pd.read_csv("./given-files/OEC_sample_input.csv", header=None)
starting_condition = output.Output(data.values[0])

data = pd.read_csv("./given-files/OEC_sample_ouput.csv", header=None)
input = input.Input(data.values[0])

print("end")