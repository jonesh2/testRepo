def mySearch(theList, anItem):
    for i in range(len(theList)):
        if theList[i] == anItem:
            print("Found: " + str(anItem))
            return
    print("Sad")
    return

def main():
    aList = []
    for i in range(400):
        aList.append(i * 3 // 2 + (50%(i+1)))
    mySearch(aList, 8)
    
main()
    