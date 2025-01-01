#yassine's solution
# def removeDuplicates(nums):
#     for i in range(len(nums)):
#         if(i == len(nums)):
#             break
#         for j in range(len(nums)):
#             j = i + 1
#             if(j == len(nums)):
#                 break
#             if(nums[i] == nums[j]):
#                 if(j == len(nums) - 1 ) :
#                     break
#                 nums[j] = nums[j+1]
#                 del nums[j+1]
#             j = j + 1
#     return len(nums)
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
# def removeDuplicates(nums):         #solution looks fine but not accepted on leetcode 
#     nums = list(set(nums))
#     print(nums)
#     return len(nums)

# = removeDuplicates([1,1,2])
# = removeDuplicates([0,0,1,1,1,2,2,3,3,4])
k=removeDuplicates([1,1]) 
print(k) 