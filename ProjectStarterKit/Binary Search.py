def binarysearch(lst, item):
    low = 0
    high = len(lst) - 1
    found = False

    while not found:
        mid = (low+high)//2
        if lst(mid) == item:
            found = True
        else:
            