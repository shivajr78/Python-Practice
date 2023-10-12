def increment(num):
    try:
        return int(num)+1

    except:
        raise ValueError("This is not good -Shiva")

a = increment('f55')
print(a)