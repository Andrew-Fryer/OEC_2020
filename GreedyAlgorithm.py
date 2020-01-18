import Output

def clamp(n):
    return max(min(n, 0.01), -0.01)

def GreedyAlgorithm(input, ordering, prev_nuclear): # ordering is just a list of strings... :)
    demand = input.demands
    output = Output.Output(None)

    history_ratio = input.last_week[1] / input.last_week[0] - 1
    nuclear_change = clamp(history_ratio)
    input.sources["nuclear"] = prev_nuclear * (nuclear_change + 1)

    for i in range(len(ordering)):
        supply = input.sources[ordering[i]]
        amount = min(float(supply), float(demand))
        demand -= amount
        output.sources[ordering[i]] = amount

    return output