def removeDuplicates(nums):
    if not  nums:
        return 0
    for i in range(len(nums)):
        j = i + 1
        if j == len(nums) - 1:
            break
        
        if nums[i] == nums[j]:
            nums[j] = nums[j+1]
            del nums[j+1]
        j = j + 1
        

    return len(nums)



k = removeDuplicates([1,1,2])
# = removeDuplicates([0,0,1,1,1,2,2,3,3,4])
#k=removeDuplicates([1,1]) 
print(k) 
