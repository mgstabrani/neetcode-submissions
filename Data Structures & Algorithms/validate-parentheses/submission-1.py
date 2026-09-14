class Solution:
    def isValid(self, s: str) -> bool:
        stack = [s[0]]
        for i in range(1, len(s)):
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                stack.append(s[i])
            elif len(stack) == 0:
                stack.append(s[i])
            else:
                if s[i] == ")" and stack[-1] == "(":
                    stack.pop()
                elif s[i] == "}" and stack[-1] == "{":
                    stack.pop()
                elif s[i] == "]" and stack[-1] == "[":
                    stack.pop()
                else:
                    stack.append(s[i])
        return len(stack) == 0