class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and ((c.islower() and stack[-1].isupper() and c == stack[-1].lower()) or (c.isupper() and stack[-1].islower() and c.lower() == stack[-1])):
                stack.pop()
            else:
                stack.append(c)

        return "".join(stack)