# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]

from typing import DefaultDict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        result = DefaultDict(list) # mapping charCount to list of anagrams

        for s in strs:
            count = [0] * 26 # a ... z

            for c in s:
                count[ord(c) - ord("a")] += 1 

            result[tuple(count)].append(s)

        return result.values()

    print(groupAnagrams(any, strs = [""]))
    print(groupAnagrams(any, strs = ["a"]))
    print(groupAnagrams(any, strs = ["eat","tea","tan","ate","nat","bat"]))