import random

def median(arr):
    arr_order = sorted(arr)
    center = len(arr_order) // 2
    
    if len(arr_order) % 2 == 1:
        return arr_order[center]
    return arr_order[center - 1], arr[center]


for q in range(1, 10+1):
    x = random.randint(1, 50+1)
    y = random.randint(1, 50+1)
    z = random.randint(1, 50+1)
    arr = [x, y, z]
    print(f"{q:<2}) {arr} — {median(arr)}")
