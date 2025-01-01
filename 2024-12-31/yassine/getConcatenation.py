def getConcatenation(nums):
    n = len(nums)
    ans  = [0] * (n * 2)
    print(ans)
    #ans = []
    for i in range(n):
        ans[i] = nums[i]
        ans[i+n] = nums[i]
    return ans 

l = [1,2,1]
a = getConcatenation(l)
print(a)