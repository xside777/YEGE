f=open('17_23952.txt')
l=[int(num) for num in f]
a=max([num for num in l if num%100==93])
r=[]
for num1,num2 in zip(l,l[1:]):
    if ((num1>a and num2<a)or(num2>a and num1<a))and(str(num1)[0]=='9' or str(num2)[0]=='9'):
        r.append(num1)
        r.append(num2)
print(len(r))
sum=0
for x in r:
    if x>a:
        sum+=x
print(len(r)//2,sum)
        
