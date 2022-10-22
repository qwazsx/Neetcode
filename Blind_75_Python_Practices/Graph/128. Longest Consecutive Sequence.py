# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

 

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
 

# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        hashset = set(nums)
        longest_streak = 0

        for num in nums:
            if num-1 not in hashset: #start of a sequence
                current_streak = 0

                while num + current_streak in hashset:
                    current_streak = current_streak +1

                longest_streak = max(current_streak, longest_streak)

        return longest_streak
        

    print(longestConsecutive(any,nums = [0,3,7,2,5,8,4,6,0,1]))