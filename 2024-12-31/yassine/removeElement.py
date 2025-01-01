def removeElement(nums, val):
    nums.sort()
    ind = 0
    for i in range(len(nums)):  
        # if nums[i] == val:
        #     del nums[i]
        if nums[i] != val:
            nums[ind] = nums[i] 
            ind = ind + 1
    return ind

l = [3,2,2,3]

v = 3
k = removeElement(l, v)
print(k)