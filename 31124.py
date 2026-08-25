f=open('17_31124.txt')
l=[int(num) for num in f]
a=min([num for num in l if num%33==0 and num>0])
count=0
r=[]
for num1,num2 in zip(l,l[1:]):
    if (num1!=num2)and(abs(num1-num2)%a==0):
        count+=1
        r.append(num1+num2)
print(count,max(r))
