# Lists
animals = ['cat', 'dog', 'monkey']
animals.append('fish');    print(animals)
animals.remove('fish');    print(animals)
animals.insert(1, 'fish'); print(animals)
animals.pop(1);            print(animals)

for i in enumerate(animals):
    print(i)

squares = [x * 2 for x in animals]
print(squares)

list1 = [12, 45, 32, 55]
list1.sort();    print(list1)
list1.reverse(); print(list1)

# Tuples
T = (1, 2, 3)
print(T + (4, 5))
t = (42,)
tuple1 = (12, 45, 32, 55, [1, 0, 3])
try:
    tuple1[0] = "good"
except TypeError as e:
    print("Error:", e)
tuple1[4][0] = 2
print(tuple1)

# Dictionaries
x = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}
d = x.copy()
d['color'] = 'red'
print(x)
print(d)
try:
    print(d['name'])
except KeyError as e:
    print("KeyError:", e)
print(d.get('name'))
print(d.get('name', 'The key value does not exist.'))
print(d.keys())
print(d.values())
print(d.items())
d.clear()
print(d)
del d

# Sets
sample_set = {'Prince', 'Techs'}
print('Data' in sample_set)
sample_set.add('Data')
print(sample_set, len(sample_set))
sample_set.remove('Data')
print(sample_set)
list2 = [1, 3, 1, 5, 3]
print(list(set(list2)))
sample_set = frozenset(sample_set)