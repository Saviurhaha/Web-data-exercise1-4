def readTxt(txt_path):
    with open(txt_path) as t:
        data = t.read()
    return data


d1 = readTxt('D:\研一材料\Web data exercise2\doc\d1.txt')
d2 = readTxt('D:\研一材料\Web data exercise2\doc\d2.txt')
d3 = readTxt('D:\研一材料\Web data exercise2\doc\d3.txt')

deleteCh = '\n.,!?;\'\"/-=()0123456789'
for ch in deleteCh:
    d1 = d1.replace(ch, '')
    d2 = d2.replace(ch, '')
    d3 = d3.replace(ch, '')

d1 = d1.lower().split()
d2 = d2.lower().split()
d3 = d3.lower().split()

documentsWord = []
documentsWord.extend(d1)
documentsWord.extend(d2)
documentsWord.extend(d3)
documentsWord = set(documentsWord)
print(d1)
print(d2)
print(d3)

documents_set = dict()
documents_set["d1"] = d1
documents_set["d2"] = d2
documents_set["d3"] = d3
invert_index = dict()
for word in documentsWord:
    temp = []
    for setKey in documents_set.keys():
        w = documents_set[setKey]
        if word in w:
            temp.append(setKey)
    invert_index[word] = temp
file = open('invertDictionary.txt', 'w')
for key, value in invert_index.items():
    file.write(key)
    file.write(':')
    file.write(str(value))
    file.write('\n')


