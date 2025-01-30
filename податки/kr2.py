# xx ^ 2 = max(:xx)

def getRange(n):
    if n % 2 == 0:
        floor = 10
        ceiling = 99+1
    else: 
        floor = 100
        ceiling = 999+1
    return floor, ceiling

def getPower(n, x):
    match n % 4:
        case 0 | 1:
            return x * x
        case 2 | 3:
            return x * x * x

def getLastNums(n):
    if n % 2 == 0:
        return -2
    else: 
        return -3

def ownExersice(n):
    floor, ceiling = getRange(n)
    nums = []
    if n%5 == 2 or n%5 == 4:
        counter = 0
    else:
        counter = 1

    for x in range(floor, ceiling):
        current_num = getPower(n, x)
        if current_num >= floor or current_num <= ceiling:
            #print(x)
            if int(str(current_num)[getLastNums(n):]) == x:
                #print(current_num)
                match n % 5:
                    case 0 | 1:
                        nums.append(current_num)
                    case 2:
                        counter += current_num
                    case 3:
                        counter *= current_num
                    case 4:
                        counter += 1
    
    match n % 5:
        case 0:
            print(f"Мінімальне число: {min(nums)}")
        case 1:
            print(f"Максимальне число: {max(nums)}")
        case 2:
            print(f"Сума чисел: {counter}")
        case 3:
            print(f"Добуток чисел: {counter}")
        case 4:
            print(f"Кількість чисел: {counter}")

for n in range(1, 24+1):
    print(f"{n}:")
    ownExersice(n)
