"""Create a function that takes a list of numbers. Return the largest number in the list.
Examples

findLargestNum([4, 5, 1, 3]) ➞ 5

findLargestNum([300, 200, 600, 150]) ➞ 600

findLargestNum([1000, 1001, 857, 1]) ➞ 1001"""

def findLargestNum(nums):
    return max(nums)

print(findLargestNum([4, 5, 1, 3]))
print(findLargestNum([300, 200, 600, 150]))
print(findLargestNum([1000, 1001, 857, 1]))

def findLargestNum(nums):

    swapped = True

    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i + 1] < nums[i]:
                swapped = True
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
        
    return nums[-1]

print(findLargestNum([4, 5, 1, 3]))
print(findLargestNum([300, 200, 600, 150]))
print(findLargestNum([1000, 1001, 857, 1]))

def findLargestNum(nums):
    return sorted(nums)[-1]

print(findLargestNum([4, 5, 1, 3]))
print(findLargestNum([300, 200, 600, 150]))
print(findLargestNum([1000, 1001, 857, 1]))
                