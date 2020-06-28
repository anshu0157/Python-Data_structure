'''
1.it is time complexity of O(N^2)
2.It is also a comparison based sorting
3.it is an inplace sorting (doesnt need an extra memory)
4.it is stable sorting and also adaptive sorting
it is alomost same as selection sort in terms of complexity
5 it is also called as online sorting for smallar data
'''
def Insertion_sort(arr):
    for i in range(len(arr)):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            #temp = arr[j]
            #arr[j] = arr[j-1]
            #arr[j-1] = temp
            arr[j],arr[j-1]=arr[j-1],arr[j]
            j = j-1

    return arr
#ls=[5,23,8,9,4,3,89,12,78,30,89,25,3,4]
ls=list(map(int,input('enter the array:').split()))
print(Insertion_sort(ls))