class Solution:
    def isValid(self, s: str) -> bool:
        p_map = {
            "}" : "{",
            "]" : "[",
            ")" : "("
        }

        stack = []

        for c in s:
            if c in p_map:
                if not stack or stack[-1] != p_map[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        
        return len(stack) == 0