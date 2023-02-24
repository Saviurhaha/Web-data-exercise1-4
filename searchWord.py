import re


def search(word):
    fr = open('invertDictionary.txt', 'r')
    for line in fr:
        v = line.strip().split(':')
        if word == v[0]:
            print(v[0] + ":" + v[1])
            return
    print('No match dictionary')
    fr.close


inputWord = input("Please input your words!")
inputWord = inputWord.split()
for word in inputWord:
    search(word)
