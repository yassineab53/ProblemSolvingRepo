def removeDuplicates(nums):
    for i in range(len(nums)):
        if(i == len(nums)):
            break
        for j in range(len(nums)):
            j = i + 1
            if(j == len(nums)):
                break
            if(nums[i] == nums[j]):
                if(j == len(nums) - 1 ) :
                    break
                nums[j] = nums[j+1]
                del nums[j+1]
            j = j + 1
    return len(nums)

#k = removeDuplicates([1,1,2])
# k = removeDuplicates([0,0,1,1,1,2,2,3,3,4])
k = removeDuplicates([1,1])
print(k)