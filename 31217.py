f=open('1.txt')
l=[list(map(int,nums.split())) for nums in f]
count=0
for nums in l:
    nums2=[num for num in nums if nums.count(num)==2]
    nums1=[num for num in nums if nums.count(num)==1]
    if len(nums2)==4 and len(nums1)==2:
        if sum(nums2)>sum(nums1):
            count+=1
print(count)
