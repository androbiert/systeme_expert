from django.shortcuts import render
from aima.logic import FolKB
from .main import get_recommendations, impliment_facts , get_final

def home(request):
    result = input_process(request=request)
    return render(request, 'EnergyCost/bar.html', {'result': result})

def PageProcess(request):
    return render(request,'EnergyCost/Form_Process.html')


def input_process(request):
    result = []
    if request.method == 'POST':
        kb = FolKB()
        facts = []
        #agenda
        facts.append('House(House)')
        num_rooms = int(request.POST.get('rooms', 0))  # Default to 0 if not provided or invalid
        fact1 = f'Number_of_rooms(House, {"Many" if num_rooms > 3 else "Few"})'
        facts.append(fact1)

        lighting = request.POST.get('lighting')
        if lighting == 'incandescent':
            facts.append('Uses_incandescent_bulbs(House)')

        insulation_quality = request.POST.get('insulation_quality')
        if insulation_quality:
            facts.append(f'Insulation(House, {insulation_quality.capitalize()})')

        appliance_efficiency = request.POST.get('appliance_efficiency')
        if appliance_efficiency:
            facts.append(f'Efficiency_appliances(House, {appliance_efficiency.capitalize()})')

        HVAC = request.POST.get('HVAC')
        if HVAC == 'old':
            facts.append('Old_HVAC_system(House)')

        windows = request.POST.get('windows')
        if windows:
            facts.append(f'Pane_windows(House, {windows.capitalize()})')

        renewable = request.POST.get('renewable')
        if renewable == 'yes':
            facts.append('Feasible_renewable_integration(House)')

        smart_home = request.POST.get('smart_home')
        if smart_home == 'yes':
            facts.append('Smart_home_feasible(House)')

        maintenance = request.POST.get('maintenance')
        if maintenance == 'yes':
            facts.append('Maintenance_needed(House)')

        unoccupied = request.POST.get('unoccupied')
        if unoccupied == 'yes':
            facts.append('Unoccupied_room(House)')

        impliment_facts(kb=kb,facts=facts)
        recommendations = get_recommendations(kb=kb)
        result = get_final(recommendations=recommendations)
        return result
    return None

