def finder(N):
    a = (N+23)%5+3
    b = (N+17)%5+3
    count = 0
    for q in range(1, 100+1):
        if q % a == 0 and q % b != 0:
            count += 1
    return count

N = 19
print(finder(N))