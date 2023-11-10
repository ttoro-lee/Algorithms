n = int(input())

nums = list(map(int, input().split()))

s = int(input())

def solution(n, nums, s):

    pt = 0
    remain = s

    while(remain and pt < n-1):

        if remain > n:
            
            tmp = max(nums[pt+1:n])

            if nums[pt] > tmp:
                pt += 1
            else:
                swap = nums.index(tmp)
                nums.remove(tmp)

                if pt == 0:
                    nums = [tmp] + nums[pt:]
                else:
                    nums = nums[:pt] + [tmp] + nums[pt:n]

                remain = remain - (swap - pt)
                pt += 1
        else:

            tmp = max(nums[pt+1:pt+remain+1])

            if nums[pt] > tmp:
                pt += 1
            else:
                swap = nums.index(tmp)
                nums.remove(tmp)

                if pt == 0:
                    nums = [tmp] + nums[pt:]
                else:
                    nums = nums[:pt] + [tmp] + nums[pt:pt+remain+1] + nums[pt+remain+1:]

                remain = remain - (swap - pt)
                pt += 1



    return nums

print(*solution(n,nums,s))
