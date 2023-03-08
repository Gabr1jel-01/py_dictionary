vehicles = {
    1 : ['Kamion', 'Iveco', 'OS 001 ZZ', 2015, 45_000],
    2 : ['Kamion', 'Iveco', 'OS 002 ZZ', 2015, 47_000]
}

print('Prije .clear()')
for key,value in vehicles.items():
    print(key, end=' ')
    for element in value:
        print(element, end=' ')
    print()    
        
vehicles.clear()

print('Poslije .clear()')
for key,value in vehicles.items():
    print(key, end=' ')
    for element in value:
        print(element, end=' ')
    print()    
        








vehicles = {
    1 : ['Kamion', 'Iveco', 'OS 001 ZZ', 2015, 45_000],
    2 : ['Kamion', 'Iveco', 'OS 002 ZZ', 2015, 47_000]
}

print('Prije .pop()')
for key,value in vehicles.items():
    print(key, end=' ')
    for element in value:
        print(element, end=' ')
    print()    
        
dict_pop_value = vehicles.pop(2)

print('Poslije .pop()')
for key,value in vehicles.items():
    print(key, end=' ')
    for element in value:
        print(element, end=' ')
    print()    
    
print(dict_pop_value)

# pop vraca samo value a key ne 









vehicles = {
    1 : ['Kamion', 'Iveco', 'OS 001 ZZ', 2015, 45_000],
    2 : ['Kamion', 'Iveco', 'OS 002 ZZ', 2015, 47_000]
}

print('Prije .popitem()')
for key,value in vehicles.items():
    print(key, end=' ')
    for element in value:
        print(element, end=' ')
    print()    
        
dict_popitem_value = vehicles.popitem()

print('Poslije .popitem()')
for key,value in vehicles.items():
    print(key, end=' ')
    for element in value:
        print(element, end=' ')
    print()    
    
print(dict_popitem_value)


vehicles = {
    1 : ['Kamion', 'Iveco', 'OS 001 ZZ', 2015, 45_000],
    2 : ['Kamion', 'Iveco', 'OS 002 ZZ', 2015, 47_000]
}

print('Prije .copy()')
print(vehicles)

vehicles_copy = vehicles.copy()
vehicles_copy[3] = 'Pero Peric'

print('Poslije .copy()')
print(vehicles)
print(vehicles_copy)
