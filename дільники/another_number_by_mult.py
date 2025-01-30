class Numbers:
    def __init__(self,num):
        self.num = num
    
    def getMults(self):
        q = 1
        arr = []
        while q**2 < self.num:
            if self.num % q == 0:
                arr.append(q)
                if q != self.num // q:
                    arr.append(self.num // q)
            q += 1
        arr.sort()
        if arr:
            arr.pop(len(arr)-1)
        return arr

    def getSum(self):
        arr = self.getMults()
        res = 0
        for q in arr:
            res += q
        return res
    
def cycle1(n1):
    
    while True:
        if n1.num in memory:
            return memory[n1.num]
        mem.append(n1.num)

        n2 = Numbers(n1.getSum())
        #print(f" • Числа:  {n1.num}, {n2.num}")
        #print(f" ○ Массив: {n1.getMults()}, {n2.getMults()}")
        if n1.num == n2.getSum() and n2.num == n1.getSum():
            return f"{n1.num}, {n2.num}"
        n1.num += 1
        #for q in mem:
        #    memory[q] = f"{n1.num}, {n2.num}"
    
    
def cycle2(n1, memory, mem):
    while True:
        if n1.num in memory:
            return memory[n1.num]
        mem.append(n1.num)

        n2 = Numbers(n1.getSum())
        n3 = Numbers(n2.getSum())
        n4 = Numbers(n3.getSum())
        n5 = Numbers(n4.getSum())
        #print(f" • Числа:  {n1.num}, {n2.num}, {n3.num}, {n4.num}, {n5.num}")
        #print(f" ○ Массив: {n1.getMults()}, {n2.getMults()}, {n3.getMults()}, {n4.getMults()}, {n5.getMults()}")
        if n1.num == n2.getSum() and n2.num == n3.getSum() and n3.num == n4.getSum() and n4.num == n5.getSum() and n5.num == n1.getSum():
            break

        n1.num += 1
    for q in mem:
        memory[q] = f"{n1.num}, {n2.num}, {n3.num}, {n4.num}, {n5.num}"

    return f"{n1.num}, {n2.num}, {n3.num}, {n4.num}, {n5.num}"


memory = {}
mem = []
for q in range(0, 10000+1):
    #print(f"{q}: {cycle1(Numbers(q))}")
    print(f"{q}: {cycle2(Numbers(q), memory, mem)}")