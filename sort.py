<<<<<<< HEAD
def sortMyList(myList):
    newList = myList.copy()
    quicksort(newList, 0, len(newList))
    return newList

def sort(myList, start, end):
=======
def partition(myList, start, end):
    pivot = myList[start]
    left = start+1
    right = end
    done = False
    while not done:
        ## Do something here
    return right

def quicksort(myList, start, end):
>>>>>>> 6cf2e6916bdfafd631759d2e4d944929f060f17b
    if start < end:
        # partition the list
        pivot = partition(myList, start, end)
        # sort both halves
        quicksort(myList, start, pivot-1)
        quicksort(myList, pivot+1, end)
        
def swap(myList, one, two):
    temp=myList[one]
    myList[one]=myList[two]
    myList[two]=temp        

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



def main():
    myList = [3, 2, 9, 0, 7, 3, 5, 11]
    sort(myList, 0, len(myList)-1)
    print myList

main()
