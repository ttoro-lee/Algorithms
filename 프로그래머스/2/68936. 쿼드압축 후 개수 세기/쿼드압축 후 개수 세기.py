def solution(arr):
    n = len(arr)
    answer = [[-1] * n for _ in range(n)]
    zero_cnt, one_cnt = 0, 0
    visited = set()
    
    k = n
    
    while(k > 0):
        for i in range(0, len(arr), k):
            for j in range(0, len(arr[0]), k):
                if (i,j) not in visited:
                    e, tmp = q_zip(arr, i, j, k)
                    if e == 0:
                        zero_cnt += 1
                    elif e == 1:
                        one_cnt += 1
                    visited.update(tmp)
        k = k // 2
        
    # print(answer)
    
    return [zero_cnt, one_cnt]


def q_zip(arr, l, m, n):
    zero_cnt = 0
    one_cnt = 0
    visited = []
    
    for i in range(l, l+n):
        for j in range(m, m+n):
            if arr[i][j] == 1 and zero_cnt == 0:
                one_cnt +=1
                visited.append((i,j))
            elif arr[i][j] == 0 and one_cnt == 0:
                zero_cnt += 1
                visited.append((i,j))
            else:
                return -1, []
            
    if zero_cnt == n**2:
        return 0, visited
    elif one_cnt == n**2:
        return 1, visited
    else:
        return -1, []
    