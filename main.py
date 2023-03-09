from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    num_dict = {}
    for i, num in enumerate(nums):
        val = target - num
        if val in num_dict:
            return [num_dict[val], i]
        num_dict[num] = i
    return []
