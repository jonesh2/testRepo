def mySearch(theList, anItem):
    return recursiveSearch(theList, 0, len(theList)-1, anItem)

def recursiveSearch(theList, left, right, anItem):
    if right < left:
        return False
    else:
        mid = (right+left)//2
        if theList[mid] == anItem:
            return True
        elif anItem > theList[mid]:
            return recursiveSearch(theList, mid+1, right, anItem)
        else:
            return recursiveSearch(theList, left, mid-1, anItem)

def main():
    aList = ["apple", "jacks", "peanuts", "quail", "snail", "tilapia", "town", "zebra"]
    print(mySearch(aList, "peanuts"))
    
main()
    