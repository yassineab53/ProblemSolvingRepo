# 26. Remove Duplicates from Sorted Array

## Problem Description

**Difficulty**: Easy

Given an integer array `nums` sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in `nums`.

Consider the number of unique elements of `nums` to be `k`. To get accepted, you need to do the following things:

1. Change the array `nums` such that the first `k` elements of `nums` contain the unique elements in the order they were present in `nums` initially.
2. The remaining elements of `nums` are not important, as well as the size of `nums`.
3. Return `k`.

### Custom Judge:

The judge will test your solution with the following code:

```java
int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
```

If all assertions pass, then your solution will be accepted.

---

## Examples

### Example 1:

**Input**: 
```
nums = [1,1,2]
```

**Output**:
```
2, nums = [1,2,_]
```

**Explanation**: 
Your function should return `k = 2`, with the first two elements of `nums` being `1` and `2` respectively. It does not matter what you leave beyond the returned `k` (hence they are underscores).

### Example 2:

**Input**:
```
nums = [0,0,1,1,1,2,2,3,3,4]
```

**Output**:
```
5, nums = [0,1,2,3,4,_,_,_,_,_]
```

**Explanation**: 
Your function should return `k = 5`, with the first five elements of `nums` being `0`, `1`, `2`, `3`, and `4` respectively. It does not matter what you leave beyond the returned `k` (hence they are underscores).

---

## Constraints

- `1 <= nums.length <= 3 * 10^4`
- `-100 <= nums[i] <= 100`
- `nums` is sorted in non-decreasing order.

---

## Solutions

### Yassine's Solution

#### Python
```python
def removeDuplicates(nums):
    if not nums:
        return 0

    k = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[k] = nums[i]
            k += 1
    return k
```

#### Java
```java
public int removeDuplicates(int[] nums) {
    if (nums.length == 0) return 0;
    int k = 1;
    for (int i = 1; i < nums.length; i++) {
        if (nums[i] != nums[i - 1]) {
            nums[k] = nums[i];
            k++;
        }
    }
    return k;
}
```

### Ayoub's Solution

#### Python
```python
def removeDuplicates(nums):
    return len(set(nums))
```

#### Java
```java
public int removeDuplicates(int[] nums) {
    return (int) Arrays.stream(nums).distinct().count();
}
```

---

## Approach

### Algorithm
1. Traverse the input array `nums`.
2. Identify duplicate elements and overwrite them in-place to ensure that each unique element appears only once.
3. Keep a counter `k` to track the number of unique elements.
4. Return `k` as the count of unique elements.

### Complexity Analysis

- **Time Complexity**: `O(n)` where `n` is the length of the input array. The algorithm involves a single traversal of the array.
- **Space Complexity**: `O(1)` because the solution modifies the input array in place and uses only a constant amount of extra space.

---

## Files in the Repository

- `README.md`: A README file describing the problem, approach, and complexity analysis.
- `yassine_solution.py`: Contains Yassine's Python solution.
- `yassine_solution.java`: Contains Yassine's Java solution.
- `ayoub_solution.py`: Contains Ayoub's Python solution.
- `ayoub_solution.java`: Contains Ayoub's Java solution.
