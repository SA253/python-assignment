l=['a','b','c','d','e','f']
print(len(l))
print(max(l))
print(min(l))
l.append('g')
print(l)
l2=['h','i','j','k','l']
l.extend(l2)
print(l)
l.insert(2,'z')
print(l)
print(l.pop(2))
print(l)
print(l.pop())
print(l)
l.remove('a')
print(l)
l.reverse()
print(l)
l.sort()
print(l)
l.sort(reverse=True)
print(l)