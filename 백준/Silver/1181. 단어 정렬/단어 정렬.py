# 길이가 짧은 것부터
# 길이가 같으면 사전 순으로

n = int(input())

dictionary = set()

for i in range(n):
    문자 = input()

    dictionary.add(문자)

dictionary = list(dictionary)

for 문자 in sorted(dictionary, key=lambda x: (len(x), x)):
    print(문자)