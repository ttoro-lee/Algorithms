import sys

string = sys.stdin.readline().strip()

def solution(string):

    string = string.replace('XXXX', 'AAAA')
    string = string.replace('XX', 'BB')

    if 'X' in string:
        return -1
    else:
        return string

print(solution(string))