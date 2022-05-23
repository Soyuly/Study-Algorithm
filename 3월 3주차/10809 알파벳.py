import sys

word = list(sys.stdin.readline().strip())
alphabet = [-1] * 26

for i in range(len(word)):
    if alphabet[ord(word[i]) - 97] == -1:
        alphabet[ord(word[i]) - 97] = i

for i in alphabet:
    print(i, end=' ')