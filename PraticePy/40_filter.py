def greater_than_5(num):
    if num>5:
        return True
    else:
        return False

l = [9,8,1,3,6,8,2,4,7,8]
print(list(filter(greater_than_5,l))) #print all greater than 5


# by using Lambda function
g10 = lambda l : l>7
print(list(filter(g10,l)))