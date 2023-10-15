from itertools import product

def solution(users, emoticons):
    answer = []
    
    # 자신의 기준에 따라 일정 비율 이상 할인 임티 모두 구매
    # 구매 비용 합이 일정 이상, 모두 취소 후 플러스 가입
    
    discounts = [10,20,30,40]
    k = len(emoticons)
    
    for discount in list(product(discounts, repeat=k)):
        all_buy = 0
        all_subscribe = 0
        for user in users:
            buy = 0
            subscribe = 0
            for idx, dc in enumerate(discount):
                if dc >= user[0]:
                    buy += (100 - dc) / 100 * emoticons[idx]
                    if buy >= user[1]:
                        buy = 0
                        subscribe = 1
                        break
            all_subscribe += subscribe
            all_buy += buy
        answer.append((all_subscribe, all_buy))
        
    answer.sort(key=lambda x:(-x[0], -x[1]))
    
    return answer[0]