import sys

n = int(sys.stdin.readline()) # 크레인 n대
hooks = list(map(int, sys.stdin.readline().split())) # 무게 제한
m = int(sys.stdin.readline()) # 박스 m개
boxs = list(map(int, sys.stdin.readline().split())) # 박스 무게들


def solution(n, hooks, m, boxs):

    answer = 0

    hooks.sort(reverse=True)
    boxs.sort(reverse=True)

    if hooks[0] < boxs[0]:
        return -1

    else:
        while(len(boxs)):
            for hook in hooks:
                if boxs and hook < boxs[-1]: # 현재 크레인이 가장 작은 박스보다 작다면
                    # 더이상 서치하지 않음
                    continue
                for box in boxs:
                    if hook >= box:
                        boxs.remove(box)
                        break
            answer += 1

    return answer


print(solution(n, hooks, m, boxs))