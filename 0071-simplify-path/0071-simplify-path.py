class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        paths = path.split("/")

        for part in paths:
            if part == "..":
                if stack:
                    stack.pop()
            elif part and part != ".":
                stack.append(part)

        final_path = "/" + "/".join(stack)
        return final_path