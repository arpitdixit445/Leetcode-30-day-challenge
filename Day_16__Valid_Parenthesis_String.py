'''
Problem Statment ->
    Given a string containing only three types of characters: '(', ')' 
    and '*', write a function to check whether this string is valid. 
    We define the validity of a string by these rules:

    *   Any left parenthesis '(' must have a corresponding right
        parenthesis ')'.
    *   Any right parenthesis ')' must have a corresponding left 
        parenthesis '('.
    *   Left parenthesis '(' must go before the corresponding right 
        parenthesis ')'.
    *   '*' could be treated as a single right parenthesis ')' or a 
        single left parenthesis '(' or an empty string.
    *   An empty string is also valid.

Example 1 ->
    Input: "()"
    Output: True    
'''

#Solution - Using Stack : Time O(n), Space O(n)


class Solution:
    def checkValidString(self, s: str) -> bool:
        if s=="":
            return True
        
        stack = []
        star = []
        for i,ch in enumerate(s):
            if ch == "(":
                stack.append(i)
            elif ch == ")":
                if not stack and not star:
                    return False
                if stack:
                    stack.pop()
                else:
                    star.pop()
            else:
                star.append(i)
                  
        while stack and star:
            if stack.pop()>star.pop():
                return False
            
        return len(stack) ==0