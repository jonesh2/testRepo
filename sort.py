def sort(myList, start, end):
    if start < end:
        # partition the list
        pivot = partition(myList, start, end)
        # sort both halves
        quicksort(myList, start, pivot-1)
        quicksort(myList, pivot+1, end)

def partition(myList, start, end, left, right):
    pivot = myList[start]
    notDone = True
    while notDone:
        while left <= right and myList[left] <= pivot:
            left = left + 1
        while myList[right] >= pivot and right >=left:
            right = right -1
        if right < left:
            done= True
        else:
            # swap places
            swap(myList, left, right)
    # swap start with myList[right]
    swap(myList, start, right)
    return right

def swap(myList, one, two):
    temp=myList[one]
    myList[one]=myList[two]
    myList[two]=temp        

def main():
    myList = [3, 2, 4, 0, 7, 3, 5, 11]
    sort(myList, 0, len(myList)-1)
    print myList

main()
