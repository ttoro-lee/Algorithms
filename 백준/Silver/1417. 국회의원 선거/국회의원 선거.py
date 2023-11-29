import sys, heapq

n = int(sys.stdin.readline().strip())

nums = []

for _ in range(n):
    nums.append(int(sys.stdin.readline().strip()))


def solution(nums):

    answer = 0

    if n == 1:
        return answer

    first = nums[0]
    pk = nums[1:]

    heap = []

    for k in pk:
        heapq.heappush(heap, -k)

    while(first <= -heap[0]):

        tmp = -(heapq.heappop(heap))

        tmp -= 1
        answer += 1
        first += 1

        heapq.heappush(heap, -tmp)

    return answer


print(solution(nums))
