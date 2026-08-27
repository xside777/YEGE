f=open('9_27284.txt')
l=[list(map(int,nums.split()))for nums in f]
count=0
for nums in l:
    numsmin=[num for num in nums if num==min(nums)]
    numsothers=[num for num in nums if nums.count(num)==1]
    if ((len(numsmin)==2)or(len(numsmin)==3))and((len(numsothers)==3)or(len(numsothers)==4)):
        if (max(numsothers)+min(numsothers))>sum(numsothers)-max(numsothers)-min(numsothers):
            count+=1
print(count)
    
