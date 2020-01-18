import Output
def GreedyAlgorithm(input, ordering): # ordering is just a list of strings... :)
    demand = input.demands
    output = Output.Output(None)

    for i in range(len(ordering)):
        supply = input.sources[ordering[i]]
        amount = min(float(supply), float(demand))
        demand -= amount
        output.sources[ordering[i]] = amount

    # TODO: nuclear is special

    return output