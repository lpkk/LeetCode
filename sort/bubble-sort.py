from typing import List
"""
冒泡排序：
比较相邻的元素。如果第一个比第二个大，就交换他们两个。
对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
针对所有的元素重复以上的步骤，除了最后一个。
持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
"""
def bubble_sort(nums:List[int] )->List[int]:
    for i in range(0, len(nums)):
        for j in range(0, len(nums)-i-1):
            if nums[j] > nums[j + 1]:
                nums[j + 1], nums[j] = nums[j], nums[j + 1]
    return nums
 
if __name__ == '__main__':
    print(bubble_sort([1,7,4,3,2,0]))
    print(bubble_sort([4,2,45,3,2]))
