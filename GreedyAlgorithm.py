import Output
def GreedyAlgorithm(input, ordering): # ordering can just be a list of strings... :)
    input_dict = {input}
    demand = input.demands
    output = Output.Output(None)
    output_dict = {}

    for i in range(len(ordering)):
        supply = input_dict[ordering[i]]
        amount = min(supply, demand)
        demand -= amount
        output_dict[ordering[i]] = amount

    # copy output_dict into output
    output.solar = output_dict
    output.solar = output_dict
    output.solar = output_dict
    output.solar = output_dict
    output.solar = output_dict
    output.solar = output_dict
    output.solar = output_dict

    print("hello")

print("end")