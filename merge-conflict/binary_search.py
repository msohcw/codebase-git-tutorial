def binary_search(start, end, search):
    mid, count = start - 1, 0
    while start < end:
        mid += 1
        print("Try {}...".format(mid))
        count += 1
        if mid == search: break
        if mid > search:
            end = mid
        else:
            start = mid
    print("Took {} tries to find {}".format(count, mid))
