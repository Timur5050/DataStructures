from implementation import BestDataStructure

map = BestDataStructure()
map.set(1, 1)
map.set(2, 2)
map.set(3, 3)
map.set(4, 4)
map.set(5, 5)

for i in range(1, 6):
    print(map.get(i), end=' ')

map.setAll(7)
print()
for i in range(1, 6):
    print(map.get(i), end=' ')
map.set(2, 5)
print()
for i in range(1, 6):
    print(map.get(i), end=' ')
print()
print(map.get(7))
map.set(6, 4)
for i in range(1, 7):
    print(map.get(i), end=' ')
print()