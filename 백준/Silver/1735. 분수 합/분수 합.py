import sys, math

분자1, 분모1 = map(int, sys.stdin.readline().split())

분자2, 분모2 = map(int, sys.stdin.readline().split())

분자 = 분자1 * 분모2 + 분자2 * 분모1
분모 = 분모1 * 분모2

최대공약수 = math.gcd(분자, 분모)

print(분자 // 최대공약수, 분모 // 최대공약수)