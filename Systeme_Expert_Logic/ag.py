from aima3.utils import expr
from aima3.logic import FolKB, fol_fc_ask

# Define the knowledge base
kb = FolKB()

x = expr('x')  


kb.tell(expr('Fever(x) & Cough(x) ==> Flu(x)')) 
kb.tell(expr('Fever(x) & BodyAches(x) & Fatigue(x) ==> Flu(x)'))  
kb.tell(expr('SoreThroat(x) & RunnyNose(x) ==> Cold(x)'))  

# Define the agenda
agenda = []


patient = expr('Alex') 
kb.tell(patient)
kb.tell(expr('Cough(Alex)'))
kb.tell(expr('Fever(Alex)'))

agenda.append(expr('Fever(Alex)'))
agenda.append(expr('Fatigue(Alex)'))
agenda.append(expr('BodyAches(Alex)'))
agenda.append(expr('Cough(Alex)'))
agenda.append(expr('Leginjury(Alex)'))
agenda.append(expr('Flu(Alex)'))


memory = {}

# Run the expert system
seen = set() 
while agenda:
    p = agenda.pop(0)
    if p in seen:
        continue 
    seen.add(p)
    if list(fol_fc_ask(kb,p)) :
        print(f'{p } is true.')
        memory[p] = True
    else:
        print(f'{p} is false.')
        memory[p] = False

    # Check if new rules can be activated
    if memory.get(expr('Fever(Alex)'), False) and memory.get(expr('Cough(Alex)'), False) :
        agenda.append(expr('Flu(Alex)'))
    if memory.get(expr('Fever(Alex)'), False) and memory.get(expr('BodyAches(Alex)'), False) and memory.get(expr('Fatigue(Alex)'), False) :
        agenda.append(expr('Flu(Alex)'))
    if memory.get(expr('SoreThroat(Alex)'), False) and memory.get(expr('RunnyNose(Alex)'), False):
        agenda.append(expr('Cold(Alex)'))

# Check the final state of the memory
print('Final diagnosis:')
for p, value in memory.items():
    if value:
        print(f'{p}')