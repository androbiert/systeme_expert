
from aima.logic import FolKB, expr, fol_fc_ask


def contain(expr,word):

    for i in range(len(expr)):
        j=i 
        mot = ''
        while(j < len(expr)):
            mot += expr[j]
            j += 1
            if mot == word :
                return True
    return False
        


def forward_chaining_with_suggestions(kb):
    inferred = set()
    agenda = kb.clauses[:]

    while agenda:
        rule = agenda.pop(0)

        # Check if the rule is an implication
        if contain(rule.to_String ,'==>'):
            premise = rule.args[0]
            conclusion = rule.args[1]
            
            # Check if the conclusion matches the desired pattern
            if conclusion.op.startswith('Suggest_'):
                inferred.add(conclusion)
            
            new_inferred = fol_fc_ask(kb, premise)
            if new_inferred:
                new_inferred = set([frozenset(item.items()) for item in new_inferred]) - inferred
                agenda.extend(new_inferred)
                inferred |= new_inferred

    return inferred


# Example usage
kb = FolKB()

kb.tell(expr('House(House)'))
kb.tell(expr('Uses_incandescent_bulbs(House)'))
kb.tell(expr('Insulation(House, Poor)'))
kb.tell(expr('Efficiency_appliances(House, Low)'))
kb.tell(expr('(Uses_incandescent_bulbs(x) & House(x)) ==> Increase_heat_output(x)'))
kb.tell(expr('(Uses_incandescent_bulbs(x) & House(x)) ==> High_energy_consumption(x)'))
#Rule .. 
kb.tell(expr('High_energy_consumption(house) ==> High_energy_usage(house)  '))
# Add example rules
kb.tell(expr('(Insulation(x, Poor) & High_energy_consumption(x)) ==> Suggest_upgrade_insulation(x)'))
kb.tell(expr('(Efficiency_appliances(x, Low) & High_energy_usage(x)) ==> Suggest_upgrade_appliances(x)'))
kb.tell(expr('(Other_condition(x)) ==> Suggest_something_else(x)'))
kb.tell(expr('(Yet_another_condition(x)) ==> Suggest_another_thing(x)'))

suggestions = forward_chaining_with_suggestions(kb)
print("All Suggestions:")
for suggestion in suggestions:
    print(suggestion)





