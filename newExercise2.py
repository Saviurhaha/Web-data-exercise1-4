import re
from functools import reduce

all_words = []
docu_set = dict()


def readTxt(i):
    with open(f"D:\研一材料\Web data exercise2\doc\d{i}.txt") as f:
        sentence = f.readline()
        sentence = sentence.strip('.')
    word = sentence.lower().split()
    all_words.extend(word)
    docu_set[f"d{i}"] = word


def buildInvertIndex(invert_index):
    dictionaryWord = set(all_words)
    for b in dictionaryWord:
        temp = []
        for j in docu_set.keys():
            f = docu_set[j]
            if b in f:
                temp.append([j, f.count(b)])
        invert_index[b] = temp
    return invert_index


def writeTxt(dic):
    with open("./invertDictionary.txt", 'w') as f:
        f.truncate(0)
        for key, value in invert_index.items():
            f.write(key)
            f.write(':')
            f.write(str(value))
            f.write('\n')


def search(word):
    with open("./invertDictionary.txt", 'r') as f:
        for line in f:
            countMap = line.strip().split(':')
            if word == countMap[0]:
                print(word+":[DocumentID,count]")
                print(countMap[1])
                files = re.findall(r"\d+\.?\d*", countMap[1])
                return files
        print("No match!")
        return 0


# def findIntersect(*array):
#     sets = iter(map(set, array))
#     result = sets.next()
#     for s in sets:
#         result = result.intersection(s)
#     return result


def intersectionFun(f1, f2):
    p1 = 0
    p2 = 0
    res = []
    try:
        while p1 < len(f1) and p2 < len(f2):
            if f1[p1] == f2[p2]:
                res.append(f1[p1])
                p1 += 1
                p2 += 1
            elif f1[p1] < f2[p2]:
                p1 += 1
            else:
                p2 += 1
        print("The intersection is in file " + str(res).strip('[]'))
    except(TypeError):
        print("No intersection!")
    return res


if __name__ == '__main__':
    for i in range(1, 4):
        readTxt(i)
    invert_index = dict()
    invert_index = buildInvertIndex(invert_index)
    writeTxt(invert_index)
    inputTwoWord = input("Input words!")
    wordElement = inputTwoWord.split(' ')
    f = []
    for i in wordElement:
        file = search(i)
        f.append(file)
    intersectionFun(f[0], f[1])

