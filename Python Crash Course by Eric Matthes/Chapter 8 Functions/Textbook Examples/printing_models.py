def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left. 
    Move each design to completed models after printing. 
    """
    
    while unprinted_designs: 
        current_designs = unprinted_designs.pop()
        print(f"printing model: {current_designs}")
        completed_models.append(current_designs)
        
def show_completed_models(completed_models): 
    """show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
        
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)