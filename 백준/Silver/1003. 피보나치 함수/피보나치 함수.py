T = int(input())

cases = []

def make_fibo(n):

    fibo = [[1,0], [0,1]]

    if n <= 1:
        return fibo
    else:
        for i in range(2, n+1):
            one = fibo[i-1][1] + fibo[i-2][1]
            zero = fibo[i-1][0] + fibo[i-2][0]
            fibo.append([zero, one])

        return fibo

for _ in range(T):

    tmp = int(input())

    cases.append(tmp)

for case in cases:
    
    fibo = make_fibo(case)

    print(fibo[case][0], fibo[case][1])


