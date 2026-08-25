from string import *
l=printable[:27]
count=0
a=2*2187**567+729**566-2*243**565+81**564-2*27**563-6561
s=''
while a>0:
    s=str(l[a%27])+s
    a//=27
s=list(map(int,s))
for i in s:
    if s[i]>9 and s[i]%2==0:
        count+=1
print(count)
