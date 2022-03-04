vocales = ['a', 'e', 'i', 'o', 'u']
for i in range(len(vocales), 1, -1):
    if i % 3 == 0:
        vocales.pop(i-1)
print(vocales)