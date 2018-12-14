#data_structure
names = ['santosh','roshan','sabuz',]
print(names)
#indexing
names = ['santosh','roshan','sabuz',]
print(names[2])
print(names[1])
#negative indexing
names = ['santosh','roshan','sabuz',]
print(name[-1])
print(name[-5])
#membership test
'santosh'in names
'om' in names
'om' not in name
#aviable method in list
a = []
dir(list)[-11:]
dir(a)
#.append(obj)
names = ['santosh','roshan','sabuz',]
names.append('dipendra')
print(names)
#.copy()
names = ['santosh','roshan','sabuz',]
abc = names
print(id(abc))
print(id(names))
#in case of mutable object same memory adrres is pointed by different alias
names = ['santosh','roshan','sabuz',]
abc = names
mno = abc.copy
print(id(abc))
print(id(names))
print(id(mno))
mno.append('radhe shyam')
print(mno)
print(names)
print(id(mno))
#.count(obj)
names = ['santosh','roshan','sabuz',]
names.count('roshan')
#.extend(list_obj)
names = ['santosh','roshan','sabuz',]
extra_names = ['dipandra','nima','radhe shyam']
names.extend(extra_names)
print(names)
#insert(index,obj)
names = ['santosh','roshan','sabuz',]
names.insert(3,'om')
#pop()
names = ['santosh','roshan','sabuz',]
names.pop()
names
names.pop(2)
names
#remove()
names = ['santosh','roshan','sabuz',]
names.remove('sabuz')
names
#reverse()
names = ['santosh','roshan','sabuz',]
names.reverse()
names
#sort()
names = ['santosh','roshan','sabuz','dawa','nima']
names.sort()
names
nmaes.sort(reverse=True)
#for loop using
names = ['santosh','roshan','sabuz','dawa','nima']
for name in names:
	print(name)
#next pattern(enumerate)
names = ['santosh','roshan','sabuz','dawa','nima']
for i in enumerate(names,1):
	print(i)
#unpacking
print('sn|','value|','length|')
for index, value in enumerate(names, 1):
	print(value,index)

