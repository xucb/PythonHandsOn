def bulid_person(first_name,last_name):
    """return a dictionary, it contains a person information"""
    person= {'first': first_name,'last':last_name}
    return person
musician= bulid_person('jimi','hendrix')
print(musician)


def bulid_person(first_name,last_name,age=None):
    """return a dictionary"""
    person = {'first': first_name,'last':last_name}
    if age:
        person['age']= age
    return person
musician=bulid_person('jimi','hendrix')
print(musician)
musician1 =bulid_person('first','last',age=27)
print(musician1)

