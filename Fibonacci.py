import time
def timeit(func):
    def timed(*args, **kw):
        ts = time.time()
        result = func(*args, **kw)
        te = time.time()
        print(te-ts)
        return result
    return timed

def fibonacci(n):
    seq =[1,1]
    while seq[-1] < n:
        seq.append(seq[-1]+ seq[-2])
    return seq
@timeit

def nthfibonacci(n):
    seq = [1,1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq[-1]

@timeit
def dynamic_fibonacci(n):
    # Taking 1st two fibonacci nubers as 0 and 1
    FibArray = [0, 1]

    while len(FibArray) < n + 1:
        FibArray.append(0)

    if n <= 1:
        return n
    else:
        if FibArray[n - 1] == 0:
            FibArray[n - 1] = fibonacci(n - 1)

        if FibArray[n - 2] == 0:
            FibArray[n - 2] = fibonacci(n - 2)

        FibArray[n] = FibArray[n - 2] + FibArray[n - 1]
    return FibArray[n]




print(dynamic_fibonacci(100))
print(nthfibonacci(100))