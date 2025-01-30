def numToArr(num):
    new_num = []
    
    while num > 0:
        new_num.append(num % 10)
        num //= 10
    new_num.reverse()

    return new_num

def sum_and_count(N):
    count = 0
    suma = 0
    for q in range(100, 999+1):
        num = numToArr(q)
        if num[2] * (N+1) == num[0] * num[1]:
            count += 1
            suma += q
            print(q)
        #print(count, q, num, suma)
    return count, suma

N = 19

count, suma = sum_and_count(N)
print(f"Кількість: {count}\nСума: {suma}")