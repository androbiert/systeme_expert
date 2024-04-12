from location import get_geocode
from aima.logic import FolKB, expr, fol_fc_ask
from weather import wheather as wh

kb = FolKB()


# Rule 1: If uses incandescent bulbs, then increase heat output
kb.tell(expr('(Uses_incandescent_bulbs(x) & House(x)) ==> Increase_heat_output(x) & High_energy_consumption(house)'))

# Rule 2: If poor insulation and high energy consumption, recommend upgrading insulation
kb.tell(expr('(Insulation(house, Poor) & High_energy_consumption(house)) ==> suggest_actions(house, "upgrade insulation")'))

#Rule .. 
kb.tell(expr('High_energy_consumption(house) ==> High_energy_usage(house)  '))

# Rule 3: If low appliance efficiency and high energy usage, recommend upgrading appliances
kb.tell(expr('(Efficiency_appliances(house, Low) & High_energy_usage(house)) ==> suggest_actions(house, "upgrade appliances")'))

# Rule 4: If uses incandescent bulbs and high heat output, recommend switching to LED bulbs
kb.tell(expr('(Uses_incandescent_bulbs(house) & Increase_heat_output(house)) ==> suggest_actions(house, "switch to LED bulbs")'))

# Rule 5: If the house has single-pane windows, recommend energy-efficient windows
kb.tell(expr('(Pane_windows(house, Single)) ==> Energy_loss(house)'))

# Rule 6: If the house has old HVAC system, indicate temperature variations
kb.tell(expr('(Old_HVAC_system(house)) ==> Temperature_variations(house)'))

# Rule 7: If a room is unoccupied, suggest energy savings
kb.tell(expr('(Unoccupied_room(house)) ==> Energy_loss(house)'))

# Rule 8: If excess renewable energy is available, suggest cost savings
kb.tell(expr('(Excess_renewable_energy(house)) ==> Cost_savings(house)'))


# Heating/Cooling System Recommendation
kb.tell(expr('(old_HVAC_system(house) & house(house)) ==> upgrade_HVAC_system(house)'))

# Rule 11: If high peak energy usage is detected, recommend optimizing energy usage
kb.tell(expr(' High_energy_usage(house) ==> Optimize_energy_usage(house)'))

kb.tell(expr('Optimize_energy_usage(house) ==> '))

# Rule 12: If renewable energy integration is feasible, recommend integrating renewable energy
kb.tell(expr('(Feasible_renewable_integration(house)) ==> Integrate_renewable_energy(house)'))

# Rule 13: If smart home automation is feasible, recommend implementing smart home features
kb.tell(expr('(Smart_home_feasible(house)) ==> Implement_smart_home(house)'))

# Rule 14: If regular maintenance is needed, recommend performing regular maintenance
kb.tell(expr('(Maintenance_needed(house)) ==> Perform_regular_maintenance(house) '))

# Rule 15: If the temperature is low, suggest using heating systems
kb.tell(expr('(Temperature(low)) ==> Integrate_heating_systems(house)'))

# Rule 16: If the temperature is high, suggest cooling methods
kb.tell(expr('(Temperature(high)) ==> Integrate_cooling_methods(house)'))

# Rule 17: If the temperature is moderate, suggest energy-saving strategies
kb.tell(expr('(Temperature(moderate)) ==> Integrate_energy_saving(house)'))

# Lighting Recommendation
kb.tell(expr('(uses_incandescent_bulbs(house) & house(house)) ==> switch_to_LED(house)'))

# Heating/Cooling System Recommendation
kb.tell(expr('(old_HVAC_system(house) & house(house)) ==> upgrade_HVAC_system(house)'))

# Regular Maintenance Recommendation
kb.tell(expr('(maintenance_needed(house) & house(house)) ==> perform_regular_maintenance(house)'))

# Rule linking number of rooms to house size
kb.tell(expr('(Number_of_rooms(house, Many) & House(house)) ==> Vast_house(house)'))
kb.tell(expr('Vast_house(house) & Insulation(house, Poor ==> Energy_loss(house)  '))



def determine_temperature_range(temperature):
    if temperature > 30:
        return 'high'
    elif temperature > 20:
        return 'moderate'
    else:
        return 'low'



# Get weather data
given_lat, given_lon = get_geocode('oran')
temperature = wh(latitude=given_lat, longitude=given_lon)[0]

# Determine temperature range based on actual temperature value
temperature_range = determine_temperature_range(temperature)

# Assert temperature range as a fact in the knowledge base
kb.tell(expr(f'Temperature({temperature_range})'))



def get_recommendations(kb):
    recommendations_fc = fol_fc_ask(kb, expr('suggest_actions(house, action)'))
    return list(recommendations_fc)



# Get recommendations based on conditions and intermediate rules
recommendations = get_recommendations(kb)
print(f"Recommendations based on conditions and intermediate rules:{recommendations}")