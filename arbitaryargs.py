def intro(*args):
    for i in args:
        i=i+1
        print(" ",i,sep="$", end=" ")
    return
intro(2,5,7,8,12)
