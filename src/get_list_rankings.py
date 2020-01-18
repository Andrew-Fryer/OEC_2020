#Power generation list ranking generator

#Constants for different 
A = 0.75
B = 2
C = 2

power_generators = ['nuclear', 'solar', 'wind', 'hydro', 'coal', 'bio', 'neighbor']

co2_emissions = [6, 105, 13, 4, 909, 58, 258] #g/kWh
cost = [68, 481, 133, 57, 140, 131, 160] #$/MWh

green_score = lambda x: (A, 1)[x in ['solar', 'wind', 'hydro', 'bio']]    
co2_score = lambda x: (1-(x/(B*max(co2_emissions))))
cost_score = lambda x: (1-(x/(C*max(cost))))

scores = []
for p in range(len(power_generators)):
    scores.append(green_score(power_generators[p]) * co2_score(co2_emissions[p]) * cost_score(cost[p]))
    print(power_generators[p], scores[p])
