def solution(numbers):
    
    return [num + ((num ^ (num + 1)) >> 2) + 1 for num in numbers]