#7-8
sandwich_orders =['Sa','Sb','Sc','Sd','Sb','Sc','Sa','Sb']
finished_sandwiches=[]

while sandwich_orders:
    finished_sandwich=sandwich_orders.pop()
    print(f"I made your {finished_sandwich}.")
    finished_sandwiches.append(finished_sandwich)

print(f"\nBelow sandwiches are made: ")
for finished_sandwich in finished_sandwiches:
    print (finished_sandwich)

#7-9
sandwich_orders =['Sa','Sb','Sc','Sd','Sb','Sc','Sa','Sb']
finished_sandwiches=[]
lack_material = 'Sb'
print(f"Warring: material {lack_material} is out of store!!! \n")
while lack_material in sandwich_orders:
    sandwich_orders.remove(lack_material)

while sandwich_orders:
    finished_sandwich=sandwich_orders.pop()
    print(f"I made your {finished_sandwich}.")
    finished_sandwiches.append(finished_sandwich)

print(f"\nBelow sandwiches are made: ")
for finished_sandwich in finished_sandwiches:
    print (finished_sandwich)


#7-10
dream_place={}

active=True

while active:
    name=input("What is your name? ")
    response = input("What is your dream place to visit? ")
    dream_place[name]=response
    
    repeat= input("Do you want others to poll? (yes/no)")    
    if repeat == 'no':
       active=False    

print("\n---below is the polling result---")
for name,response in dream_place.items():
    print(f"{name} would like to visit {response}.")