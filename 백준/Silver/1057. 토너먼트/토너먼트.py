# N명 토너먼트
# 1 ~ N 번까지 배정
# 인접한 번호끼리 스타
# 이긴 사람 진출
# 진 사람 탈락

# 홀수면, 마지막 번호 자동 진출

# 번호는 다시 1번부터
# 한명 남을때까지 반복

# 김지민, 임한수 (임한수와 언제 대결)

n, kim, lim = map(int, input().split())

nums = list(range(1,n+1))

def solution(nums):

    answer = 1
    k = len(nums)

    while(k != 1):

        tmp = []

        if k % 2 == 1:
            for i in range(0,k,2):
                if i == k-1:
                    tmp.append(nums[i])
                else:
                    if nums[i] in (kim, lim) and nums[i+1] in (kim, lim):
                        return answer
                    else:
                        if nums[i] in (kim, lim):
                            tmp.append(nums[i])
                        elif nums[i+1] in (kim, lim):
                            tmp.append(nums[i+1])
                        else:
                            tmp.append(nums[i])
        else:
            for i in range(0,k,2):
                if nums[i] in (kim, lim) and nums[i+1] in (kim, lim):
                        return answer
                else:
                    if nums[i] in (kim, lim):
                            tmp.append(nums[i])
                    elif nums[i+1] in (kim, lim):
                        tmp.append(nums[i+1])
                    else:
                        tmp.append(nums[i])
        answer += 1
        nums = tmp
        k = len(nums)

    return -1

print(solution(nums))

