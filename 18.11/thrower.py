def cycle(select):   
    def throwerA(n):
        s = str(n)
        return int(s[-1:] + s[:-1])

    def throwerB(n):
        s = str(n)
        return int(s[1:] + s[0])
    
    n = 10 ** 7
    limit = 10 ** 8
    
    for q in range(n, limit):
        if select == 2:
            choose = throwerA(q)
        elif select == 3:
            choose = throwerB(q)
        
        if q*select == choose:
            return f"Відподвідь: {q}"

print(cycle(2))