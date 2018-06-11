#using regular expression to search pattern from a text files
import re

def mainn():
    file = open('DeepLearning.txt','r')
    #lines = file.read().splitlines()
    lines=file.readlines()
    for line in lines:
        if re.search('(learn|comput)ing', line):
            print(line, end='\n\n')
mainn()
