name="MISSISSIPPI"
k={}
for i in name:
    if i not in k:
        k[i]=1
    else:
        k[i]=k[i]+1
print(k)