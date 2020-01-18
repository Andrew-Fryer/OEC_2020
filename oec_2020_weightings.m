A = 0.75;
B = 2;
C = 2;

Max_CO2_Emissions = 909; %g/kWh
Max_Cost = 481; %$/MWh
Energies = ["solar","wind","hydro","bio","nuclear","gas","neighbour"]; %bio=geothermal, gas=coal
Energy_Constant = [0,0,0,0,0,0,0];
C02_Power_Constant = [105, 13, 4, 58, 6,909,258];%g/kWh
Cost_Power_Constant = [481,133,57,131,68,140,160];%MWh

CO2_source = @(CO2_emissions) (1 - (CO2_emissions/(B*Max_CO2_Emissions)));
cost_score = @(cost) (1 - (cost/(C*Max_Cost)));

for i = 1:size(Energies,2)
    if(Energies(i) == "solar" || Energies(i) == "wind" || Energies(i) == "hydro" || Energies(i) == "bio")
        Energy_Constant(i) = 1;
    else
        Energy_Constant(i) = A;
    end
    
    Energy_Constant(i) = Energy_Constant(i)*CO2_source(C02_Power_Constant(i))*cost_score(Cost_Power_Constant(i));
    
    %Energies(i)
    %CO2_source(C02_Power_Constant(i))
    %cost_score(Cost_Power_Constant(i))
    
    
end

disp(Energies);
disp(Energy_Constant);