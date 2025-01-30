import time

def find_all_divisors_var1(N):
	res=[]
	d=1
	while d <= N:
		if N % d == 0:
			res.append(d)
		d+=1
	return res

def find_all_divisors_var2(n):
    def prime(n):
        prime_list = {}
        q = 2
        while q ** 2 <= n:
            while n % q == 0:
                if q not in prime_list:
                    prime_list[q] = 0
                prime_list[q] += 1
                n //= q
            q += 1
        if n > 1:
            prime_list[n] = 1
        return prime_list
    
    def gen(primes):
        prime_list = list(primes.items())
        div = [1]
        
        for prime, step in prime_list:
            new_div = []
            for s in range(1, step + 1):
                for d in div:
                    new_div.append(d * (prime ** s))
            div.extend(new_div)
        
        return sorted(set(div))
    
    return gen(prime(n))

def find_all_divisors_var3(n):
    res = []
    d = 1
    while d**2 <= n:
        if n % d == 0:
            res.append(d)
            if d != n // d: 
                res.append(n // d)
        d += 1
    return sorted(res)

	

number = 363636363

start=time.time()
print(find_all_divisors_var2(number)) # ~x1 (0.00037 | 0.00036)
print(time.time()-start)
