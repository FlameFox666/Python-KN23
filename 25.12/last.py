memory = []
def task1():
    res = 0
    start = 1
    end = 100
    step = 1
    for q in range(start, end+1, step):
        print(q)
        if q % 3 == 0:
            res+=1
    return res

print(task1())