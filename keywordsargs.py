def intro(**kwargs):
    for key,values in kwargs.items():
        print(key,values, sep=":")
    return
intro(name="vignesh",age=22)