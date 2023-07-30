#To get input from user as list and print numbers of times the element is present in list.
def lst(li):
    global lst
    lst = []
    n=int(input("Enter number of elements:"))
    for j in range(n):
        ele=int(input())
        lst.append(ele)
    print(lst)
lst(lst)
lst1 = {}
for i in lst:
    if i not in lst1:
        lst1[i]=1
    else:
        lst1[i]+=1
print(lst1)