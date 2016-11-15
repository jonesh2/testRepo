def partition(myList, start, end):
    pivot = myList[start]
    left = start+1
    right = end
    done = False
    while not done:
        ## Do Something here
        #
        #
        #
        #
        #
        #
        #
        #
    return right

def quicksort(myList, start, end):
    if start < end:
        # partition the list
        pivot = partition(myList, start, end)
        # sort both halves
        quicksort(myList, start, pivot-1)
        quicksort(myList, pivot+1, end)

def switch(myList, one, two):
    temp=myList[one]
    myList[one]=myList[two]
    myList[two]=temp           

def main():
    myList = [3, 2, 4, 2, 7, 7, 5, 11]  
    quicksort(myList, 0, len(myList)-1)
    print myList

main()