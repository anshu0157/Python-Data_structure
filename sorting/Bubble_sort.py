'''
1.Bubble sort has time complexity of O(N^2) in both worst and average case
2.It is also inplace sorting (it does not need any extra memory)
3.it is also comparison sorting(which needs to compare elments in an array)
'''
def Bubble_sort(arr):
    ln=len(arr)
    for i in range(ln-1):
        for j in range(ln-1-i):
            if arr[j] > arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1] = temp
    return (' '.join(arr))

ls=list(map(str,input('enter the array:').split()))
print(Bubble_sort(ls))
