class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        
        for bracket in s:
            if bracket == "(" or bracket == "{" or bracket == "[":
                stack.append(bracket)
            
            if bracket == ")":
                if not stack or stack.pop() != "(":
                    return False
            
            if bracket == "}":
                if not stack or stack.pop() != "{":
                    return False

            if bracket == "]":
                if not stack or stack.pop() != "[":
                    return False
        if not stack:
            return True
        
        return False