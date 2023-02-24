all_words = []
docu_set = dict()
stop_words = '.,!?;\'\"/-=()[]'


def read_sentence_file(i):
    with open(f"D:\研一材料\Web data exercise2\doc\d{i}.txt") as f:
        str = f.readline()
        str = str.strip('.')
    d = str.lower().split()
    all_words.extend(d)
    docu_set[f"d{i}"] = d


def build_invert_index(invert_index):
    set_all_words = set(all_words)
    for b in set_all_words:
        temp = []
        for j in docu_set.keys():
            field = docu_set[j]
            if b in field:
                temp.append([j, field.count(b)])
        invert_index[b] = temp
    return invert_index


def write_invert_index_to_file(dic):
    with open("./invert_index_dic", 'w') as f:
        # 按dic格式写入文件
        for key, value in invert_index.items():
            f.write(key)
            f.write(':')
            tmp = ""
            for i in value:
                tmp += str(i[0])
                tmp += str(" ")
                tmp += str(i[1])
                tmp += str(" ")
            f.write(tmp)
            f.write('\n')


def search_word(word):
    with open("./invert_index_dic", 'r') as f:
        for line in f:
            l = line.strip().split(':')
            # 若匹配则输出
            if word == l[0]:
                tmp = l[1].split()
                tmplist = []
                i = 0
                while i < len(tmp):
                    tmplist.append([tmp[i], tmp[i + 1]])
                    i += 2
                sorted(tmplist, key=lambda x: x[1])
                print(f"\"{word}\" is in file {[i[0] for i in tmplist]}")
                print(f"\"{word}\" in file {[i[0] for i in tmplist]} score is {[i[1] for i in tmplist]}")
                return [i[0] for i in tmplist]
        print(f"There're no match files for \"{word}\"")
        return 0


if __name__ == '__main__':
    for i in range(1, 4):
        read_sentence_file(i)
    invert_index = dict()
    invert_index = build_invert_index(invert_index)
    write_invert_index_to_file(invert_index)

    word1 = input("please input the keyword1 to search:").lower()
    f1 = search_word(word1)
    print(f1)
