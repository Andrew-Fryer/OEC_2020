import pandas as pd
import Input
import Output
import GreedyAlgorithm

files = ['inputFile1', 'inputFile2', 'inputFile3']

for f in files:
    # read in csv file
    data = pd.read_csv("../given-files/"+f+".csv", header=None)
    # replace blanks with zeros
    data = data.fillna(0)
    
    # the first 3 lines are the starting conditions
    starting_conditions = list(map(Output.Output, data.values[:3]))
    # the rest of the lines are inputs
    inputs = list(map(Input.Input, data.values[3:-1]))
    
    # Generate outputs
    outputs = []
    prev_nuclear = data.values.tolist()[2][4] # nuclear supply form last line of starting conditions
    for my_input in inputs:
        # Here, we only look at current and past data
        # Seriously, we aren't cheating at all!
    
        #ordering_from_weighting = ["hydro", "wind", "biofuel", "nuclear", "neighbor", "solar", "gas"]
        # this is the ordering_from_weighting, but with nuclear first
        ordering = ["nuclear", "hydro", "wind", "biofuel", "neighbor", "solar", "gas"]
        #ordering_ontario_current = ["nuclear", "hydro", "gas", "wind", "solar", "biofuel", "neighbor"]
    
        output = GreedyAlgorithm.GreedyAlgorithm(my_input, ordering, prev_nuclear)
        outputs.append(output.to_array(my_input))
    
        prev_nuclear = output.sources["nuclear"]
    
    # write to csv file
    out = pd.DataFrame.from_records(outputs, columns=["Output", "Time", "Total", "Solar", "Nuclear", "Wind", "Hydroelect", "Gas/oil", "Biofuel", "Neighbor", "Diff.", "Green", "Bought", "Sold", "CO2 made", "Selling Price", "Cost to Make", "Diff.", "END"])
    out.to_csv('../outputs/'+f+'.csv')