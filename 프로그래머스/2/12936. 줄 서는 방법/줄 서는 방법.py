def solution(n, k):
    answer = []
    nums = [n for n in range(1, n+1)]
    fact = factori(n)
    
    while(n != 0):
        answer.append(nums[(k-1) // fact[n-1]])
        nums.remove(answer[-1])
        k = k % fact[n-1]
        n -= 1
    
    
    return answer


def factori(n):
    
    nums = [1] * (n+1)
    
    for i in range(1, n+1):
        if i < 3:
            nums[i] = i
        else:
            nums[i] = nums[i-1] * i
            
    return nums