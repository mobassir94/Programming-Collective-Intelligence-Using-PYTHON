# writing a python code to get the most frequently word occurred in a text doccument

from collections import Counter
import re
import operator

wordcount = {}


def main():
    fp = open("DeepLearning.txt", "r+")
    for word in fp.read().split():
        if (word not in wordcount):
            wordcount[word] = 1
        else:
            wordcount[word] += 1
    x = sorted(wordcount.values(), reverse=True)
    print(x[0])
    xx=x[0]
    for keyval in wordcount.keys():
        if(wordcount[keyval] == xx):
            print(keyval)

    fp.close();


if __name__ == '__main__': main()
