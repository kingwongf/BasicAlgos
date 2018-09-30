
def BubbleSort(l):
    for i in range(len(l)-1,0, -1):
        for ind in range(i):
            if l[ind] > l[ind+1]:
                temp = l[ind]
                l[ind] = l[ind+1]
                l[ind+1] = temp
    return l

def MergeSort(l):
    if len(l)> 1:
        m = len(l)//2
        left = l[:m]
        right = l[m:]
        MergeSort(left)
        MergeSort(right)

        i =0
        j =0
        k =0

        while i < len(left) and j <len(right):
            if left[i] < right[j]:
                l[k] = left[i]
                i+=1
            else:
                l[k] =right[j]
                j+=1
            k+=1

        while i < len(left):
            l[k] = left[i]
            i+=1
            k+=1
        while j < len(right):
            l[k] = right[j]
            j+=1
            k+=1
    return l



