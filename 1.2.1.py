student_names = ['Bill', 'Frank', 'Athik', 'Ping', 'Andy', 'Ravi', 'Aamir', 'Helen', 'Daisy', 'Javagal', 'Sourav', 'Hatije', 'Oberon', 'Mary']
"""
a = 1
b = 2.6
c = [1,2,3,5,6]
d = {'kiefer':'katovich', 'dave':'yerrington'}
e = ('one', 'two', 'three')
f = {1:{'key':'value'}, 2:{'key2':'value2'}}
g = True
h = False
i = 'integer'

print (type(a))
print (type(b))
print (type(c))
print (type(d))
print (type(e))
print (type(f))
print (type(g))
print (type(h))
print (type(i))

for i in e:
    print (i)

print(student_names)
print(student_names[0])
print(student_names[len(student_names)-1])
for i in range(5):
    print (student_names[i])
print(student_names[:5])
nine_ten = student_names[8] + " " + student_names[9]
print (nine_ten)

animals = ['duck', 'rat', 'boar', 'slug', 'mammoth', 'gazelle']
animals.append("tortoise")
numbers = [0., 0.1, 1., 10., 100., 1000.]

print (animals)
print(len(animals))
print(len(animals[4])/len(animals[1]))
print(float(len(animals[4])/len(animals[1])))
print(animals + numbers)
print(animals, numbers)
animals.extend(numbers)
print(animals)

names = ['doug', 'billy', 'kiefer', 'kian', 'sam']
names[2] = 'greg'
names.insert(2, 'greg')
names.remove('kiefer')
print (names)
"""
mix = [['billy', 'sam'], {'key':'value'}, 12.999, 12, 'flower', 'a', (1, 2, 3)]
""" mix = mix.sort(mix)
print mix
mix_sort = []
for i in mix:
    mix_sort.append(str(i))
print (mix_sort)
print (mix)
print(mix.index('a'))   """
print (mix[::-1])
print(mix)
