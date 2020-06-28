'''
1.it is stable sorting
2.it has time complexity of O(NlogN) in every case
3.it is not an inplace sorting
4.This sorting is also known as best for bigger data
'''

def merge_sort(arr):
    if len(arr)==1:
        return
    middle=len(arr)//2
    left_half=arr[:middle]
    right_half=arr[middle:]
    merge_sort(left_half)
    merge_sort(right_half)
    merge(arr,left_half,right_half)

def merge(arr,left_half,right_half):
    i,j,k=0,0,0
    while i <len(left_half) and j< len(right_half):
        if left_half[i] <right_half[j]:
            arr[k]=left_half[i]
            i+=1
        else:
            arr[k]=right_half[j]
            j+=1
        k+=1
    while i<len(left_half):
        arr[k]=left_half[i]
        k+=1
        i+=1
    while j<len(right_half):
        arr[k]=right_half[j]
        k+=1
        j+=1
if __name__=='__main__':
    a=list(map(int,input().split()))
    merge_sort(a)
    print(a)