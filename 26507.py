l=[]
for x in range(1,232):
    count=0
    n=64**678+55**123-x
    while n>0:
        if n%25==0:
            count+=1
        n//=25
    l.append(count)
print(max(l))
