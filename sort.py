def quicksort(myList, start, end):
    if start < end:
        # partition the list
        pivot = #partition
        # sort both halves
        quicksort(myList, start, pivot-1)
        quicksort(myList, pivot+1, end)

def main():
    myList = [3, 2, 4, 0, 7, 3, 5, 11]
    sort(myList, 0, len(myList)-1)
    print myList

main()