def findBigestNum(nums):
    bigest = nums[0]
    for i in nums:
        if i > bigest:
            bigest = i
    return(bigest)

def findSecondBiggestNum(nums):
    bigest = findBigestNum(nums)
    secondbigest = nums[0]
    for i in nums:
        if i > secondbigest and i != bigest :
            secondbigest = i
    return(secondbigest)

def findLowernum(nums):
    Lower = nums[0]
    for i in nums:
        if i < Lower:
            Lower = i
    return(Lower)

def findSecondLowernum(nums):
    Lower = findLowernum(nums)
    secondLower = nums[0]
    for i in nums:
        if i < secondLower and i != Lower:
            secondLower = i
    return(secondLower)



listnum = [4,5,17,3,2,0,9,10,15,16]

print(findBigestNum(listnum))
print(findSecondBiggestNum(listnum))
print(findLowernum(listnum))
print(findSecondLowernum(listnum))
print(max(listnum))
print(min(listnum))