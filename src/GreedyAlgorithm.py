import Output

# clamp value to be between limits (-0.01 to 0.01)
def clamp(n):
    return max(min(n, 0.01), -0.01)

# greedily use power supplies in the order of ordering
def GreedyAlgorithm(input, ordering, prev_nuclear): # ordering is just a list of strings... :)
    demand = input.demands # running total of demand that needs to be covered
    output = Output.Output(None) # create blank output object

    # Some cool logic to predict how much nuclear power we should commit to using
    history_ratio = input.last_week[1] / input.last_week[0] - 1
    nuclear_change = clamp(history_ratio)
    input.sources["nuclear"] = prev_nuclear * (nuclear_change + 1)

    for i in range(len(ordering)):
        # here's the greedy part
        supply = input.sources[ordering[i]]
        amount = min(float(supply), float(demand))
        demand -= amount
        output.sources[ordering[i]] = amount

    return output