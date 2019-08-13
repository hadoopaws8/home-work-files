                    #selection sort selected positions are swaping


def sort(nums):

    for i in range(5):
        minpos = i
        for j in range(i,6):
            if nums[j]<nums[minpos]:
                minpos=j
        temp=nums[i]
        nums[i]=nums[minpos]
        nums[minpos]=temp

        print(nums)


nums=[4,2,1,7,6,5,9]
sort(nums)
print(nums)
