from itertools import combinations

x = int(input())

def solution(x):

    nums = []

    for i in range(1, 11):
        tmp = list(combinations(range(10), i))
        num = [list(n) for n in tmp]

        for n in num:
            nums.append(int(''.join(sorted(list(map(str, n)), reverse=True))))



    nums.sort()
        


    if len(nums) > x:
        return nums[x]
    else:
        return -1
    
print(solution(x))
    


