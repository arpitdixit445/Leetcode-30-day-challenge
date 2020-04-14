'''
Problem Statement ->
      You are given a string s containing lowercase English letters, 
      and a matrix shift, where shift[i] = [direction, amount]:

        * direction can be 0 (for left shift) or 1 (for right shift). 
        * amount is the amount by which string s is to be shifted.
        * A left shift by 1 means remove the first character of s and append it to the end.
        * Similarly, a right shift by 1 means remove the last character of s and add it to the beginning.
        * Return the final string after all operations.
        
Example ->
      Input: s = "abcdefg", shift = [[1,1],[1,1],[0,2],[1,3]]
      Output: "efgabcd"
      Explanation:  
      [1,1] means shift to right by 1. "abcdefg" -> "gabcdef"
      [1,1] means shift to right by 1. "gabcdef" -> "fgabcde"
      [0,2] means shift to left by 2. "fgabcde" -> "abcdefg"
      [1,3] means shift to right by 3. "abcdefg" -> "efgabcd"
'''

#Solution - Using Python Slicing : Time O(n*m), Space O(n)

class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        temp = s
        for i in shift:
            direction = i[0]
            degree = i[1]
            temp = self.shifting(temp,degree,direction)
        return temp
        
    def shifting(self, string, degree,direction):
        string = list(string)
        newstring = []
        size = len(string)
        if degree > size:
            degree = degree%size 
        point = size-degree
        if direction == 0:
            point = degree
        
        newstring += string[point:]
        newstring += string[:point]
        return "".join(newstring)
