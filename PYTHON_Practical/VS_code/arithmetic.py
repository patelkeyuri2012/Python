def add(a, b):
    if(a<0) or (b<0):
        k = print("\nPlease enter only postive and valid numbers for addition")
    else:
        k = (a+b)
    return(k)

def sub(a, b):
    if(b>a or a<0 or b<0):
        k = print("\nPlease enter only postive and valid numbers for substraction")
    else:
        k = (a-b)
    return(k)

def mul(a, b):
    if(a<=0) or (b<=0):
        k = print("\nPlease enter only postive and valid numbers for multiplication")
    else:
        k = (a*b)
    return(k)

def div(a, b):
    if(b>a or a<=0 or b<=0):
        k = print("\nPlease enter only positive and valid numbers for division")
    else:
        k = (a/b)
    return(k)
    
