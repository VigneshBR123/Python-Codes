a=input("Enter your name:")
freq={}
for i in a:
    if i not in freq:
        freq[i]=1
    else:
        freq[i]+=1
print(freq)