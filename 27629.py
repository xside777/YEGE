f=open('17_27629.txt')
l=[int(num) for num in f]
a=max([num for num in l if (len(str(num))==4) and num%100==43])
print(a)
r=[]
for num1,num2 in zip(l,l[1:]):
    if (len(str(abs(num1)))==4 or len(str(abs(num2)))==4)and(((num1+num2)**2)<(a**2)):
        r.append((num1+num2)**2)
print(len(r),max(r))
