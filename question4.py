list1=["one","two","three","four"]
list2=[1,2,3,4]
a={}
for i in range (len(list1)):
    a[list1[i]]=list2[i]
print(a)