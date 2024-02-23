def badge_maker(name):
    return f'Hello, my name is {name}.'

def batch_badge_creator(names):
    l = []
    for x in names:
        l.append(f'Hello, my name is {x}.')

    return l

def assign_rooms(names):
    l = []

    for i in range(len(names)): 
        l.append(f'Hello, {names[i]}! You\'ll be assigned to room {i + 1}!')

    return l

def printer(names):

    for i in range(len(names)): 
        print(f'Hello, my name is {names[i]}.')

    for i in range(len(names)): 
        print(f'Hello, {names[i]}! You\'ll be assigned to room {i + 1}!')
