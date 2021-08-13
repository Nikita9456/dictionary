dict1={"nikita":78,"priya":23,"kirti":56,"teena":32,"usha":90,"mona":65}
s=sorted(dict1.values())
p={}
for i in s:
    for k in dict1.keys():
        if dict1[k]==i:
            p[k]=dict1[k]
            break

print(p)# i=0
# k=[]
# while i<len(n):
#     if i<2:
#         k.update(k)
#     i=i+1
# print(k)