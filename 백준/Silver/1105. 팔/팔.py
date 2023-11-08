# L, R 입력
# 자연수 중에서 8이 가장 적게 들어있는 수 8의 개수를 구하는 프로그램

# case 1, 두 자리수가 다르다면 1, 10, 100.. 이 무조건 들어가므로 0
# case 2, 두 자리수가 같다면
# 숫자가 같다면 8의 개수 출력
# 숫자가 다르다면 앞에서부터 8을 비교, 다르면 끝

L, R = input().split()

def solution(L, R):

    if len(L) != len(R):
        return 0
    
    else:
        if L == R:
            return L.count('8')
        
        else:
            for i in range(len(L)):
                if L[i] != R[i]:
                    break
        return L[:i].count('8')
    
print(solution(L,R))

