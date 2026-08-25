f=open('17_29971(1).txt')
l=[int(num) for num in f]
a=max([num for num in l if num%100==33])
r=[]
for num1,num2,num3 in zip(l,l[1:],l[2:]):
    if ((9<abs(num1)<100)+(9<abs(num2)<100)+(9<abs(num3)<100)==2)and((num1+num2+num3)**2<a):
        r.append(num1+num2+num3)
print(len(r),max(r))
