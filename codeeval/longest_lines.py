import sys
from operator import itemgetter, attrgetter

test_cases = open(sys.argv[1], 'r')

max_count = int(test_cases.readline())

word_list = [] #(word,length)

for test in test_cases.readlines():
    test = test.strip('\n')
    word_list.append((test,len(test)))

word_list = sorted(word_list,key=itemgetter(1),reverse=True)

for i in range(0,max_count):
    print word_list[i][0]

test_cases.close()