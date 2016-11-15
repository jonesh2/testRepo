def quicksort(myList, start, end):
    if start < end:
        # partition the list
        pivot = partition(myList, start, end, start+1, end)
        # sort both halves
        quicksort(myList, start, pivot-1)
        quicksort(myList, pivot+1, end)

def main():
    myList = [3, 2, 9, 0, 7, 3, 5, 12]
    quicksort(myList, 0, len(myList)-1)
    print myList

main()
