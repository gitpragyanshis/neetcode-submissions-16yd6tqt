class Solution:
    def isValid(self, s: str) -> bool:
        m = {
            "]" : "[",
            ")" : "(",
            "}" : "{",
        }

        st = []

        for c in s:
            if c in "[{(":
                st.append(c)
            else:
                if not st or m[c] != st[-1]:
                    return False
                st.pop()
        return len(st) == 0