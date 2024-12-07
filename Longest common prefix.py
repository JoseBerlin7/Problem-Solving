'''
Problem - 3

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

'''
# Solution

def lcp(lst):
    lst.sort()
    x = ''
    longest_common = lst[0]
    for i in range(1,len(lst)):
        while longest_common !=  lst[i][:len(longest_common)]:
            longest_common = longest_common[:-1]
            if not longest_common:
                return ""
    return longest_common



print(lcp(['Flower','Flow', 'Flask', 'Flaw']))
print(lcp(['Flower','Flow', 'Flask', 'Slaw']))
print(lcp(['Slower','Flower', 'Flask', 'Slaw']))