n = input()


def solution(n):

    answer = ''

    # 중앙을 기준으로 앞을 자른 수 A, 뒤집은 수 A'
    # 뒤를 자른 수 B, 뒤집은 수 B'

    length = len(n)

    mid = length // 2

    if length == 1:
        C = int(n) + 1
        if C < 10:
            answer = str(C)
        else:
            answer = '11'

    elif length % 2 == 0:
        # 길이가 짝수인 경우
        # A' <= B 이면, A에 +1 값이 C일떄
        # CC' 가 정답
        r_A = n[:mid][::-1]
        A = n[:mid]
        B = n[mid:]

        if int(r_A) <= int(B):
            C = str(int(A) + 1)

            if len(A) != len(C):
                # 자리수가 변한다면
                answer = C + C[::-1][1:]
            else:
                answer = C + C[::-1]
        # A' > B
        else:
            answer = A + A[::-1]
    else:
        # 홀수인 경우
        m = n[mid]
        r_A = n[:mid][::-1]
        A = n[:mid]
        B = n[mid+1:]

        if int(r_A) <= int(B):

            C = str(int(m) + 1)

            if C == '10':
                n_A = str(int(A) + 1)
                if len(n_A) == len(A):
                    answer = n_A + '0' + n_A[::-1]
                else:
                    answer = n_A + n_A[::-1]
            else:
                answer = A + C + A[::-1]
        # A' > B
        else:
            answer = A + m + A[::-1]

    return answer


print(solution(n))
