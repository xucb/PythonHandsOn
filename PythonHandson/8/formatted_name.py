def get_formatted_name(first_name,last_name):
    """Return formatted name"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician= get_formatted_name('jimi','hendrix')
print(musician)


#make argument optional
def get_formatted_name(first_name,last_name,middle_name=''):
    """Return formatted name"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician= get_formatted_name('jimi','hendrix')
print(musician)
musician= get_formatted_name('john','hooker','lee')

print(musician)

# four parameters
#bill xu
#bill abc xu
#bill abc bcd xu

def get_formatted_name(first_name,last_name,middle_name='',second_name=''):
    """Return formatted name"""
#    if middle_name and second_name:
#        full_name = f"{first_name} {middle_name} {second_name} {last_name}"
    if middle_name and second_name:
        full_name = f"{first_name} {middle_name} {second_name} {last_name}"
    elif middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician= get_formatted_name('jimi','hendrix')
print(musician)
musician= get_formatted_name('john','hooker','lee')
print(musician)
musician = get_formatted_name('1stName','lastName','middle','mysecondname')
print (musician)
