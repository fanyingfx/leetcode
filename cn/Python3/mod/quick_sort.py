def quick_sort(arr,start,end):
    if start>=end:
        return
    p=partition(arr,start,end)
    quick_sort(arr,start,p-1)
    quick_sort(arr,p+1,end)
    return 

def partition(arr,start,end):
    pivot=arr[end]
    s=start
    for i in range(start,end):
        if arr[i]<pivot:
            arr[s],arr[i]=arr[i],arr[s]
            s+=1
    s+=1
    arr[s],arr[end]=arr[end],arr[s]
    return s


