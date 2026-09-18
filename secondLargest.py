def secondLargest(nums):
    unique = sorted(set(nums))
    if len(unique) < 2:
        return None
    return unique[-2]

nums = [ 4, 1, 7, 7, 3 ]
secondLargest(nums)
print(secondLargest(nums))