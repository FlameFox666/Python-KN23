# ФУНКЦІЯ 1: Отримую величину доходу та повертаю величину податку

# Функція 1.1: обрахування малого податку
def getLowTax(points, low):
    return points * low

# Функція 1.2: обрахування верхнього податку
def getHighTax(high_points, low_points, low, high):
    return high_points * high + getLowTax(low_points, low)

# Функція 1.3: обрахування малого податку
def getTaxValue(points, low, high, taxless_value, tax_higher_value):
    if points < taxless_value:
        return 0
    low_points = points - taxless_value
    if points < tax_higher_value:
        return getLowTax(low_points, low)
    else:
        high_points = points - tax_higher_value
        return getHighTax(high_points, low_points, low, high)

# ФУНКЦІЯ 2: Отримую величину доходу та повертаю величину податку
def getPointsAfterTax(points, tax):
    return points - tax

# ФУНКЦІЯ 3: Отримую суму після податків та вираховує початкову суму

# Функція 3.1: обрахування від малого податку
def getOriginalLowPoints(low_points, taxless_value, low):
    return low_points / (1 - low) + taxless_value

# Функція 3.2: обрахування від більшого податку
def getOriginalHighPoints(high_points, high, tax_higher_value, low):
    return (high_points / (1 - high) + (1 - low) + tax_higher_value) + 400
# Функція 3.3: обрахування від самого податку
def getOriginalPoints(points, low, high, taxless_value, tax_higher_value):
    if points < taxless_value:
        return points
    low_points = points - taxless_value
    if points < tax_higher_value:
        return getOriginalLowPoints(low_points, taxless_value, low)
    else:
        high_points = points - tax_higher_value
        return getOriginalHighPoints(high_points, high, tax_higher_value, low)

"""
points = 10000
tax_low_percent = 0.05
tax_high_percent = 0.2
taxless_value = 1000
tax_higher_value = 7000
"""
points = 24000
tax_low_percent = 0.07
tax_high_percent = 0.35
taxless_value = 600
tax_higher_value = 14000

tax = getTaxValue(points, tax_low_percent, tax_high_percent, taxless_value, tax_higher_value)
result = getPointsAfterTax(points, tax)
original_points = getOriginalPoints(result, tax_low_percent, tax_high_percent, taxless_value, tax_higher_value)

print(f"\nВхідна сума: {points}\nНижній поріг податку: {tax_low_percent}\nВерхній поріг податку: {tax_high_percent}\nПодаток: {tax}\nЗалишок: {result}\nВідновлена сума: {original_points}")
