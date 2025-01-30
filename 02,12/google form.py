"""
class Quiz:
    def __init__(self, n, a, b, c, d):
        self.n = n
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def getBounds(self):
        l = self.a[self.n % 10]
        r = self.b[self.n % 11]
        return l, r

    def mult(arr):
        res = 1
        for w in arr:
            res *= w
        return res
    
    def makeQuiz(self):
        boundL, boundR = self.getBounds()

        res = (
            f"Знайдіть кількість натуральних чисел між числами {boundL} та {boundR} ({c[self.n%2]} включаючи у границі), "
            f"які {c[(self.n//2)%2]} діляться на {self.n%10+1} {self.d[self.n%4]} {c[(self.n//3)%2]} діляться на {(self.n*self.n)%7+2}"
        )

        print(res) 

    def question1(self):
        boundL, boundR = self.getBounds()
        count = 0
        for q in range(boundL, boundR+1):
            if (q>0 and isinstance(q,int)) and q % 7 == 0 and q % 6 != 0:
                count += 1
        
        return count 

    def question2(self):
        def steps(q):
            def numbers(q):
                num = []
                while q > 0:
                    num.append(q % 10)
                    q //= 10
                return num

            match self.n % 9 + 1:
                case 1: # Остання цифра числа
                    return int(str(q)[-1])
                case 2: # Сума квадратів цифр числа
                    return sum(numbers(q**2))
                case 3: # Добуток цифр числа
                    return self.mult(numbers(q))
                case 4: # Двоцифрове число, створене зліпленням першої та останньої цифри числа
                    return int(str(q)[0] + str(q)[-1])
                case 5: # Сума цифр числа
                    return sum(numbers(q))
                case 6: # Кількість цифр числа
                    return len(str(q))
                case 7: # Перша цифра числа
                    return int(str(q)[0])
                case 8: # Сума першої та останньої цифр числа
                    return int(str(q)[0]) + int(str(q)[-1])
                case 9: # Добуток першої та останньої цифр числа
                    return int(str(q)[0]) * int(str(q)[-1])

        boundL, boundR = self.getBounds()
        count = 0

        while boundL <= boundR:
            if boundL > 0 and isinstance(boundL, int) and boundL % 7 != 0 and boundL % 6 == 0:
                count += 1

            step = steps(boundL)
            print(step)
            if step == 0:
                step = 1
            boundL += step

        return count
    
    def question3(self):
        x = self.question1()
        y = self.question2()
        count = 0
        while count * self.n+1 < y+10*x:
            count += 1 
        return count
    
    def question4(self):
        def is_prime(n):
            if n < 2:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True

        x = self.question1()
        y = self.question2()
        k = self.question3()
        
        number = self.n * (self.n + x) * (self.n + y) * (self.n + k)
        res = number + 1

        while True:
            if is_prime(res):
                return res
            else:
                res += 1

    def question5(self):
        x = self.question1()
        y = self.question2()
        k = self.question3()
        p = self.question4()
        
        text = f"{self.n}{x}{y}{k}{p}"
        step = 2 + (self.n + x + y) % 2

        res = []
        for q in range(0, len(text), step):
            res.append(int(text[q:q + step]))
        
        return res
    
    def question6(self):
        res = -1
        
        arr = self.question5()
        l = len(arr)
        turtle = l//2
        p = self.question4()

        for q in range(l - turtle + 1):
            parts = arr[q:q + turtle]

            if len(str(p)) % 2 == 0: 
                tmp = sum(parts)
            else:
                tmp = self.mult(parts)

            res = max(res, tmp)
        return res
    
    def question7(self):
        def ceasar(num, key):
            alphabet="0123456789"
            res=""

            for q in num:
                id = alphabet.find(q)
                if id!=-1:
                    id1 = id+key 
                    while id1>=len(alphabet):
                        id1-=len(alphabet)
                    w = alphabet[id1]
                    res+=w
                else:
                    res+=q

            return res
        x = self.question1()
        y = self.question2()
        k = self.question3()
        p = self.question4()
        l = len(self.question5())
        s = self.question6()

        text = f"{self.n}{x}{y}{k}{p}{l}{s}"
        key = self.n % 10 + 1
        return ceasar(text, key)

    def execute(self):
        self.makeQuiz()
        print(
            f"X   = {self.question1()}\n"
            f"Y   = {self.question2()}\n"
            f"K   = {self.question3()}\n"
            f"P   = {self.question4()}\n"
            f"Arr = {self.question5()}\n"
            f"L   = {len(self.question5())}\n"
            f"S   = {self.question6()}\n"
            f"Ces = {self.question7()}"
        )


test = Quiz(N, a, b, c, d)
test.execute()
"""

def getBounds():
    l = a[n % 10]
    r = b[n % 11]
    return l, r

def makeTest():
    print(
        f"Знайдіть кількість натуральних чисел між числами {boundL} та {boundR} ({c[n%2]} включаючи у границі), "
        f"які {c[(n//2)%2]} діляться на {n%10+1} {d[n%4]} {c[(n//3)%2]} діляться на {(n*n)%7+2}"
    )

def task1():
    l = boundL
    r = boundR
    count = 0
    for q in range(l, r+1):
        if q % 7 == 0 and q % 6 != 0:
            count += 1
    return count 

def task2():
    def steps(q):
        return int(str(q)[0]) + int(str(q)[-1])
    l = boundL
    r = boundR
    res = 0
    step = steps(l)
    for q in range(l, r+1, step):
        if not (q % 7 == 0 and q % 6 != 0):
            res += q
        step += steps(res)
    return res

def task3(n):
    count = 0
    while count * n+1 < y+10*x:
        count += 1 
    return count

def task4(n, x, y, k):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    number = n * (n + x) * (n + y) * (n + k)
    res = number + 1

    while not is_prime(res):
        res += 1
    return res

def task5(n, x, y, k, p):
    text = f"{n}{x}{y}{k}{p}"
    step = 2 + (n + x + y) % 2

    res = []
    for q in range(0, len(text), step):
        res.append(int(text[q:q + step]))
    
    return res

def task6(p, arr):
    def mult(arr):
        res = 1
        for w in arr:
            res *= w
        return res

    res = -1
    l = len(arr)
    turtle = l//2

    for q in range(l - turtle + 1):
        parts = arr[q:q + turtle]

        if len(str(p)) % 2 == 0: 
            tmp = sum(parts)
        else:
            tmp = mult(parts)

        res = max(res, tmp)
    return res

def task7(n, x, y, k, p, l, s):
    def ceasar(num, key):
        alphabet="0123456789"
        res=""

        for q in num:
            id = alphabet.find(q)
            if id!=-1:
                id1 = id+key 
                while id1>=len(alphabet):
                    id1-=len(alphabet)
                w = alphabet[id1]
                res+=w
            else:
                res+=q

        return res
    text = f"{n}{x}{y}{k}{p}{l}{s}"
    key = n % 10 + 1
    return ceasar(text, key)

n = 16
a = [1,5,16,21,32,7,3,12,11,43]
b = [51,75,116,121,232,87,93,312,211,143,120]
c = ["", "не"]
d = ["та", "або", "або", "та"]

boundL, boundR = getBounds()

makeTest()
x = task1()
y = task2()
k = task3(n)
p = task4(n, x, y, k)
arr = task5(n, x, y, k, p)
l = len(arr)
s = task6(p, arr)
ces = task7(n, x, y, k, p, l, s)
print(
    f"1. X   = {x}\n"
    f"2. Y   = {y}\n"
    f"3. K   = {k}\n"
    f"4. P   = {p}\n"
    f"5. Arr = {arr}\n"
    f"6. L = {len(arr)}\n"
    f"   S = {s}\n"
    f"7. Ces = {ces}"
)