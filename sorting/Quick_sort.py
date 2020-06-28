'''
1.it has time complexity of O(NlogN) in every situation best,average and O(N^2) in worst case
2.it is also stable and inplace sorting
3.it is '''

def swap(num,a,b):
    temp=num[a]
    num[a] =num[b]
    num[b] = temp
def partition(arr,low,high):
    pivot_i=(low + high)//2
    swap(arr,pivot_i,high)

    i=low
    for j in range(low,high):
        if arr[j] <= arr[high]: #(change the <= sign to >= sign for descending order)
            swap(arr,i,j)
            i+=1

    swap(arr,i,high)
    return i

def quick_sort(arr,low,high):
    if low>=high:
        return
    pivot=partition(arr,low,high)
    quick_sort(arr,low,pivot-1)
    quick_sort(arr,pivot+1,high)
l=[9,32,5,1,0,53,78,23,78,90,20,21]
quick_sort(l,0,len(l)-1)
print(l)