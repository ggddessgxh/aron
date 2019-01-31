nums=[2,3,4,5,6,7,8]
target=10
for i in range(0,len(nums)-1):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j]==target:
            print(i,j)
