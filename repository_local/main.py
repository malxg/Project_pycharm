def add(a,b):
    sum = a + b
    return sum

def multiple(a,b):
    result = a * b
    return result

def debug():
    sum = add(1,2)
    result = multiple(3,4)
    return sum,result

if __name__=="__main__":
    debug()
