from math import gcd

def solution(w,h):
    
    g = gcd(w, h)
    
    ww = w // g
    hh = h // g
    
    cut = ww * hh - (ww - 1) * (hh - 1)
    
    return w * h - cut * g