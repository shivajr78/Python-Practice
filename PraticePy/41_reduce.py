from functools import reduce

sum = lambda a,b : a+b

l = [1,2,4,5,0,7]
# 1+2 = 3
# 3+4 = 7
# 7+5 = 12
# 12+0 = 12
# 12+7 = 19  == val

val = reduce(sum,l)
print(val)
