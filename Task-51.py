from math import gcd
from functools import reduce

array1 = [24, 36, 48, 60]
array2 = [12, 18, 24, 36, 72]
array = array1 + array2
result = reduce(gcd, array)

print(gcd(result))
