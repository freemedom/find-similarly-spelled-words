import textdistance as td
def similar_levenshtein(a, b):
    return td.levenshtein.normalized_similarity(a,b)

from difflib import SequenceMatcher
def similar_built_in(a, b):
    return SequenceMatcher(None, a, b).ratio()

# print(similar('Genius','genius')) #0.833

find_word = input("查找类似拼写的单词，请输入要查找的单词：")
find_word = find_word.lower()

with open('./a.txt', 'r') as a:
    items = a.read().split('\n')


# 或许复杂度可以再优化，不过这里就不考虑这么多了
def method_name(similar_fun):
    print()
    print(similar_fun)

    global items # item同名会被下面修改
    similarity_dict = {}
    for i in items:
        ratio = similar_fun(i, find_word)
        similarity_dict[i] = ratio
        # print(ratio)
    sorted_similarity_dict = dict(sorted(similarity_dict.items(), key=lambda x: x[1], reverse=True))
    print("按相似度排序的前10个结果：")
    count = 0
    for item, ratio in sorted_similarity_dict.items():
        print(f"{item}: {ratio}")
        count += 1
        if count == 10:
            break


method_name(similar)
method_name(similar_levenshtein)