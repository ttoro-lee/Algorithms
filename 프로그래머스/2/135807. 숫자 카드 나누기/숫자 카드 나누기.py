from math import gcd

def solution(arrayA, arrayB):
    answer = 0
    
    a1 = find_gcd(arrayA)
    b1 = find_gcd(arrayB)
    # 조건 1
    # 철수가 가진 카드들에 적힌 모든 숫자를 나눌 수 있음
    # 영희가 가진 카드들에 적힌 모든 숫자들 중 하나도 나눌 수 없는 a
    
    # 조건 2
    # 영희가 가진 모든 카드 나눌 수 있음
    # 철수가 가진 모든 카드 나눌 수 없음 a
    
    for a, b in zip(arrayA, arrayB): # a1은 a의 최대 공약수
        if a1 != 0 and b % a1 == 0: # a1이 영희를 나눌 경우
            a1 = 0
        if b1 != 0 and a % b1 == 0: # b1이 철수를 나눌 경우
            b1 = 0
    return max(a1, b1)

def find_gcd(numbers):
    
    if len(numbers) < 2:
        return numbers[0]
    
    result = numbers[0]
    
    for i in range(1, len(numbers)):
        result = gcd(result, numbers[i])
        
    return result
