def simple_interest (p, r, n):
    i = (p * r * n) / 100
    return i

def compound_interest(p,r,n):
    amount = 1 + (p * (pow((1+r/100), n)))
    ci = amount - p
    return ci




