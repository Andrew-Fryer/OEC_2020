import Output
import math

def clamp(n):
    return max(min(n, 0.01), -0.01)
def GreedyAlgorithm(input, ordering, prev_nuclear): # ordering is just a list of strings... :)
    demand = input.demands
    output = Output.Output(None)

    # Farleyness
    nuclear_ratio = (demand * 1.025 - (float(input.sources["wind"]) + float(input.sources["hydro"]) + float(input.sources["biofuel"]))) / prev_nuclear
    history_ratio = abs(input.last_week[1] / input.last_week[0] - 1)
    nuclear_change = clamp(history_ratio * (nuclear_ratio-1) / abs(nuclear_ratio - 1))
    input.sources["nuclear"] = prev_nuclear * (nuclear_change + 1)
    if math.isnan(input.sources["nuclear"]):
        print("yo")

    for i in range(len(ordering)):
        supply = input.sources[ordering[i]]
        amount = min(float(supply), float(demand))
        demand -= amount
        output.sources[ordering[i]] = amount

    # TODO: nuclear is special

    return output