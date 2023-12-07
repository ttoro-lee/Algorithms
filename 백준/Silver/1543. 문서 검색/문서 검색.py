import sys

strings = sys.stdin.readline().strip()
finds = sys.stdin.readline().strip()


answer = strings.replace(finds, '#')

print(answer.count('#'))
