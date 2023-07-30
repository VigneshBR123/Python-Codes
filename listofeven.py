lst = []
n=int(input("Enter the number of elements:"))
for i in range(1,n+1):
    ele=int(input("Enter a {0} element:".format(i)))
    lst.append(ele)
def even(li):
    print("The even numbers are:")
    for i in li:
        if i%2==0:
             print(i)
even(lst)