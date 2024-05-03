from aima.logic import  expr, fol_fc_ask,FolKB


def impliment_facts(kb,facts):
    implement_rules(kb)
    # Add new facts to the knowledge base
    for fact in facts:
        kb.tell(expr(f'{fact}'))


# Add more rules as needed

"""
    The first Problem was that the unification between the suggestions rules :like this 
    
    
    # # Rule 2: If poor insulation and high energy consumption, recommend upgrading insulation
    # kb.tell(expr('Insulation(house, Poor) & High_energy_consumption(house) ==> Suggest_actions(house, "upgrade insulation")'))

    # # Rule 3: If low appliance efficiency and high energy usage, recommend upgrading appliances
    # kb.tell(expr('(Efficiency_appliances(house,Low) & High_energy_usage(house)) ==> Suggest_actions(house, "upgrade appliances")'))
    
    so We decide to change the entire Rule to be Unique like :
    Suggest_actions(house, "upgrade insulation") To Suggest_upgrade_insulation(house)
    
    """

def implement_rules(kb):
    kb.tell(expr('(Uses_incandescent_bulbs(x) & House(x)) ==> Increase_heat_output(x)'))
    kb.tell(expr('(Uses_incandescent_bulbs(x) & House(x)) ==> High_energy_consumption(x)'))
    kb.tell(expr('High_energy_consumption(house) ==> High_energy_usage(house)'))
    # Rule 2: If poor insulation and high energy consumption, recommend upgrading insulation
    kb.tell(expr('Insulation(house,Poor) & High_energy_consumption(house) ==> Suggest_upgrade_insulation(house)'))
    kb.tell(expr('Increase_heat_output(x) ==> Temperature_variations(x) '))
    kb.tell(expr('Increase_heat_output(x) ==> Suggest_integrate_cooling_methods(x) '))
    kb.tell(expr('Efficiency_appliances(house,Low) ==> High_energy_consumption(house)'))
    kb.tell(expr('Efficiency_appliances(house,Average) ==> High_energy_consumption(house)'))
    
    # # Rule 3: If low appliance efficiency and high energy usage, recommend upgrading appliances
    kb.tell(expr('(Efficiency_appliances(house,Low) & High_energy_usage(house)) ==> Suggest_upgrade_applaiance(house)'))

    # Rule 4: If uses incandescent bulbs and high heat output, recommend switching to LED bulbs
    kb.tell(expr('(Uses_incandescent_bulbs(house) & Increase_heat_output(house)) ==> Suggest_switch_to_LED(house)'))

    # # Rule 5: If the house has single-pane windows, recommend energy-efficient windows
    kb.tell(expr('(Pane_windows(house, Single)) ==> Energy_loss(house)'))
    kb.tell(expr('Pane_windows(house, Double)==> Insulation(house, Poor)'))

    kb.tell(expr('Energy_loss(house) ==> Suggest_energy_savings(house)'))
    # # Rule 6: If the house has old HVAC system, indicate temperature variations
    kb.tell(expr('Old_HVAC_system(house) ==> Temperature_variations(house)'))

    kb.tell(expr('Temperature_variations(house) ==> Suggest_upgrade_HVAC_system(house)'))
    # # Rule 7: If a room is unoccupied, suggest energy savings
    kb.tell(expr('(Unoccupied_room(house)) ==> Energy_loss(house)'))

    # # Rule 8: If excess renewable energy is available, suggest cost savings
    kb.tell(expr('(Excess_renewable_energy(house)) ==> Cost_savings(house)'))

    # Rule 11: If high peak energy usage is detected, recommend optimizing energy usage
    kb.tell(expr(' High_energy_usage(house) ==> Suggest_Optimize_energy_usage(house)'))

    kb.tell(expr('Suggest_Optimize_energy_usage(house) ==> Cost_savings(house)'))

    # Rule 12: If renewable energy integration is feasible, recommend integrating renewable energy
    kb.tell(expr('Feasible_renewable_integration(house) & Energy_loss(house) ==> Suggest_integrate_renewable_energy(house)'))

    # Rule 13: If smart home automation is feasible, recommend implementing smart home features
    kb.tell(expr('Smart_home_feasible(house)   ==> Implement_smart_home(house)'))

    # Rule 14: If regular maintenance is needed, recommend performing regular maintenance
    kb.tell(expr('Maintenance_needed(house) & Vast_house(house)  ==> Suggest_regular_maintenance(house) '))

    # Rule 15: If the temperature is low, suggest using heating systems
    kb.tell(expr('(Temperature(Low)) ==> Suggest_integrate_heating_systems(house)'))

    # Rule 16: If the temperature is high, suggest cooling methods
    kb.tell(expr('(Temperature(High)) ==> Suggest_integrate_cooling_methods(house)'))

    # Rule 17: If the temperature is moderate, suggest energy-saving strategies
    kb.tell(expr('(Temperature(Moderate)) ==> Suggest_energy_savings(house)'))

    # Rule linking number of rooms to house size
    kb.tell(expr('(Number_of_rooms(house, Many) & House(house)) ==> Vast_house(house)'))
    kb.tell(expr('Vast_house(house) & Insulation(house, Poor) ==> Energy_loss(house)  '))


# Define a function to determine temperature range
def determine_temperature_range(temperature):
    if temperature > 30:
        return 'high'
    elif temperature > 20:
        return 'moderate'
    else:
        return 'low'

# Get weather data and determine temperature range
# given_lat, given_lon = get_geocode('oran')
# temperature = wh(latitude=given_lat, longitude=given_lon)[0]
# temperature_range = determine_temperature_range(temperature)
# kb.tell(expr(f'Temperature({temperature_range})'))

# Initialize memory to track inferred suggestions
memory = {}
suggestions = []
suggestions.extend(['Suggest_upgrade_insulation','Suggest_upgrade_HVAC_system','Suggest_upgrade_applaiance' ,
                    'Suggest_integrate_renewable_energy', 'Suggest_switch_to_LED',
                     'Suggest_implement_smart_home',
                      'Suggest_energy_efficient_windows', 'Suggest_regular_maintenance',
                     'Suggest_energy_savings', 'Suggest_cost_savings',
                     'Suggest_regular_maintenance', 'Suggest_integrate_heating_systems',
                     'Suggest_integrate_cooling_methods','Suggest_Optimize_energy_usage'])

# Run forward chaining to infer suggestions
def get_recommendations(kb):
    memory ={}
    for suggestion in suggestions :
        result = fol_fc_ask(kb, expr(f'{suggestion}(house)'))
        if len(list(result)) > 0:
            memory[suggestion] = True
        # else:
        #     memory[suggestion] = False
    return memory

# Print out inferred suggestions

# Read and display suggestion steps from the text file
def display_suggestion_steps(suggestion):
    file_name = 'suggestion_steps.txt'
    with open(file_name, 'r') as file:
        found_suggestion = False
        result = ''
        for line in file:
            line = line.strip()
            if line == f"Suggestion: {suggestion}":
                found_suggestion = True
                
            elif line.startswith('Suggestion: '):
                found_suggestion = False
                continue
            elif found_suggestion and line:
                result += f"   {line}\n"
    return result


def get_steps(recommendations):
   
    result = []
    for suggestion, inferred in recommendations.items():
        if inferred:
            result.append(display_suggestion_steps(suggestion)) 
    return result


def parse_suggestions_file(file_name):
    suggestions_data = {}
    with open(file_name, 'r') as file:
        suggestion_title = None
        steps = []
        for line in file:
            line = line.strip()
            if line.startswith('Suggestion: '):
                if suggestion_title is not None:
                    suggestions_data[suggestion_title] = steps
                suggestion_title = line.split('Suggestion: ')[1]
                print("i am sug title" + suggestion_title)
                steps = []
            elif line.startswith('Steps to '):
                print("i am in steps of "+suggestion_title)
                continue
            else:

                steps.append(line.strip())
        if suggestion_title is not None and steps:
            suggestions_data[suggestion_title] = steps
    return suggestions_data

# Example usage
file_name = 'suggestion_steps.txt'
def get_final(recommendations):
    suggestions_data = parse_suggestions_file(file_name)
    filtered_suggestions_data = {suggestion: suggestions_data.get(suggestion, []) for suggestion in recommendations}
    return filtered_suggestions_data


# Create a dictionary for only the suggestions in suggestions_list

# print(filtered_suggestions_data)
# # Print the filtered suggestions data
# for suggestion, steps in filtered_suggestions_data.items():
#     print(f"Suggestion: {suggestion}")
#     for step in steps:
#         print(f"  - {step}")
