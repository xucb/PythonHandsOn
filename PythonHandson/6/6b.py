#6-4

favorite_number={
    'A':'4',
    'B':'2',
    'C':'9',
    'D':'10',
}


favorite_number['E']=23
favorite_number['F']=19
favorite_number['G']=1
favorite_number['H']=24

for key,value in favorite_number.items():
    print(f"{key}'s favorite number is {value}") 

#6-5
river_country={
    'nile':'egypt',
    'riverB':'countryB',
    'riverC':'countryC',
    'riverD':'countryD',
    'riverE':'countryE',
}
for river,country in river_country.items():
    print(f"The {river.title()} runs through {country.title()}.")

for river in river_country.keys():
    print(f"{river.title()}")

for country in river_country.values():
    print(f"{country.title()}")


#6-6
person_language={
    'a':'la',
    'b':'lb',
    'c':'la',
    'd':'ld',
}
person_list=['b','a','d','e','c','f']

for person in person_list:
    if person in person_language.keys():
        print(f"{person.title()}, thanks for your time!")
    else:
        print(f"{person.title()}, please take your time to join the test.")
