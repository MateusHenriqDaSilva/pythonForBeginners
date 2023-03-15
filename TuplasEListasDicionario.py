tupla = ("Homo sapiens", "Canis familiaris", "Felis Catus")
tupla
tupla.index('Canis familiaris')
for elemento in tupla:
    print(elemento)
l1 = ['Homo sapiens','Canis familiaris', 'Felis catus']
l2 = ['Xenopus laevis','Ailuropoda melanoleuca']
l3 = l1 + l2
l2
l2_2 = 12 * 2
print(l2_2)
l1[0]
l1
l1[0:2]
l1.append('Gorila gorila')
print(l1)
l1.remove('Felis Catus')
print(l1)
del(l1)
print(l1)
for item in l2_2:
    print(item)

coleta = {'aedes egypt': 32, 'Aedes albopictus': 22, 'Anopheles darlingi': 14}
coleta['aedes egypt']
coleta['Aedes albopictus'] = 11
print(coleta)
del(coleta)
print(coleta)
coleta.items()
coleta.keys()
coleta.values()
coleta2 = {'Anopheles gambiae': 13, 'Anopheles deaneorum': 11}
print(coleta2)
coleta.update(coleta2)
print(coleta)
for especie, num_especimes in coleta.items():
    print(f'especie: {especie}, numeros de especimes coletados: {num_especimes}')
biomeculas = ('proteina', 'acidos nucleos', 'carboidratos', 'lipideo', 'acidos nucleicos','carboidratos')
print(biomeculas)
print(set(biomeculas))

c1 = {1,2,3,4}
c2 = {4,3,2,1}
c3 = c1.intersection(c2)
print(c3)
c1.difference(c2)
c2.difference(c1)

