import pandas as pd
import Input
import Output
import GreedyAlgorithm

data = pd.read_csv("./given-files/inputFile1.csv", header=None)
data = data.fillna(0)

starting_conditions = list(map(Output.Output, data.values[:3]))

inputs = list(map(Input.Input, data.values[3:-1]))

outputs = []
prev_nuclear = starting_conditions[-1].sources["nuclear"]
for my_input in inputs:
    ordering_from_weighting = ["hydro", "wind", "biofuel", "nuclear", "neighbor", "solar", "gas"]
    ordering = ["nuclear", "hydro", "wind", "biofuel", "neighbor", "solar", "gas"]
    ordering_ontario_current = ["nuclear", "hydro", "gas", "wind", "solar", "biofuel", "neighbor"]

    output = GreedyAlgorithm.GreedyAlgorithm(my_input, ordering_from_weighting, prev_nuclear)
    outputs.append(output.to_array())

    prev_nuclear = output.sources["nuclear"]

print(outputs)