dict={
    "alex":["subj1","subji2","subji3"],
    "david":["subji1","subji2"]
}
count=0
for i in dict:
    if isinstance(dict[i],list):
        count+=len(dict[i])
print(count)   