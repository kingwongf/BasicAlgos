from BinarySearch import sqrt
def PrimeFactors(num):
    factors = []
    while num%2 ==0:
        factors.append(2)
        num = num/2
    for i in range(3, int(sqrt(num) + 1), 2):
        while num%i == 0:
            factors.append(i)
            num =num/i
    if num > 2:
        factors.append(num)
    return factors
