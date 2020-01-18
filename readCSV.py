import pandas as pd
import Input
import Output
import GreedyAlgorithm

data = pd.read_csv("./given-files/inputFile1.csv", header=None)

starting_conditions = map(Output.Output, data.values[:3])

inputs = map(Input.Input, data.values[3:-1])

outputs = []
for my_input in inputs:
    ordering_from_weighting = ["hydro", "wind", "biofuel", "nuclear", "neighbor", "solar", "gas"]
    ordering = ["nuclear", "hydro", "wind", "biofuel", "neighbor", "solar", "gas"]
    ordering_ontario_current = ["nuclear", "hydro", "gas", "wind", "solar", "biofuel", "neighbor"]
    my_input.sources["nuclear"] = 10781
    output = GreedyAlgorithm.GreedyAlgorithm(my_input, ordering_from_weighting)
    outputs.append(output.to_array())

print(outputs)