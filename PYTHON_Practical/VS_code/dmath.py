def mean(data):
    if len(data) == 0:
        mean = 0
    else:
        sum = 0
        for i in data :
            sum += int(i)
        mean = sum / len(data)
    return mean

def median(data):
    if len(data) == 0:
        median = 0
    sort_data = sorted(data) 
    n = len(sort_data)
    if n % 2 == 0:
        med = int(n/2)
        median = sort_data[med-1]
    else:
        med = int((n+1)/2)
        median = sort_data[med-1]
    return median

def mode(data):
    if len(data) == 0:
        mode = 0
    else:
        max_freq = 0 
        for i in data:
            freq = data.count(i)  
            if freq > max_freq :
                max_freq = freq
                f = data.index(i) 
        mode = data[f]
    return mode  