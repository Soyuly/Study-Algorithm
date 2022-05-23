import sys
from collections import Counter

word = str.upper(sys.stdin.readline().strip())

if len(word) == 1:
    print(str.upper(word))
    exit()


if Counter(word).most_common(2)[0][1] == Counter(word).most_common(2)[1][1]: 
    print("?")
else:
    print(str.upper(Counter(word).most_common(2)[0][0]))