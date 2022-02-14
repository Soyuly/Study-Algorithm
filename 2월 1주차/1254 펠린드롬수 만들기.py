#펠린드롬수는?
# 앞에서 읽을때랑 뒤에서 읽을때랑 단어가 같아야함 즉 맨 앞의 알파벳을 맨 뒤로,
# 그다음 2번재 알파벳은 뒤에서 2번째로 옮기면 될듯

# 단어 입력
word = input()

# 입력받은 단어의 글자수
len_word = len(word)

for i in range(len_word):
    flag = True
    
    # 펠린드롬수 구하는 로직
    for j in range(len_word):

        # 만약 펠린드롬수가 아니면 맨끝에서부터 문자를 하나씩 추가함
        # abcd 이면 abcda -> abcdba -> abcdcba
        if word[j] != word[-(j + 1)]:
            
            #원하는 위치에 단어 삽입
            copy = list(word) # 문자열 -> 리스트
            if i == 0:
                copy.insert(len(copy)+ 1, word[i])
            else :
                copy.insert(len(copy) - i, word[i])

            # 리스트 -> 문자열
            word = "".join(copy)             
            flag = False
            break
    
    # 펠린드롬수일때 글자수 출력
    if flag:
        print(len(word))
        break
    
    
            




