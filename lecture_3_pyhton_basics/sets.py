#initialise a set
s = set()

s.add(1)
s.add(2)
s.add(3)
s.add(4)

s.remove(2)
print(s) #{1, 3, 4}

print(f"the set has {len(s)} elements")