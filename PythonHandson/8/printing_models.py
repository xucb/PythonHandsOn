
unprinted_designs = ['phone case','robot pendant','dodecahedron']
completed_models =[]

while unprinted_designs:
    current_design = unprinted_designs.pop()
    completed_models.append(current_design)

print("\nThe follow models have been printed")
for completed_model in completed_models:
    print(completed_model)
print (completed_models)
print(unprinted_designs)






def print_models(unprinted_designs,completed_models):
    """move to list completed_models"""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"printing model: {current_design}")
        completed_models.append(current_design)
    
def show_completed_models(completed_models):
    """show all printed models"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['phone case','robot pendant','dodecahedron']
completed_models =[]

print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)