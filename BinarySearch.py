## O(log(x))
def search(l, int):

    min =0
    max = len(l) -1
    from Sorting import BubbleSort
    l = BubbleSort(l)
    while min <= max:
        m = (min + max)// 2
        if l[m] == int:
            return m
        elif l[m] < int:
            min = m + 1
        else:
             max = m - 1
    return 'no element'


## O(log(x))
def sqrt(int):
    min = 1
    max = int

    if int== 0 or int == 1: return int
    while min <= max:
        m = (min + max)//2
        if m*m == int: return m
        if m*m < int:
            min = m +1
            ans = m
        else:
            max = m -1
    return ans



# print(search([1,5,3,8,5,6,3,2,7,3,8],11))

# print(sqrt(44))
