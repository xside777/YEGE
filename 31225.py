f=open('17_31225.txt')
l=[int(num) for num in f]
a=max([num for num in l if len(str(abs(num)))==4 and num%10==9])
r=[]
for num1,num2,num3 in zip(l,l[1:],l[2:]):
    if (((num1%10==9 and len(str(abs(num1)))==4)+(num2%10==9 and len(str(abs(num2)))==4)+(num3%10==9 and len(str(abs(num3)))==4))==2)and((num1+num2+num3)<a):
        r.append(num1+num2+num3)
print(len(r),max(r),r)
