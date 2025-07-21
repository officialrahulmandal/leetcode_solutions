class Solution:
    def makeFancyString(self, s: str) -> str:
        l = len(s)
        if l <= 2:
            return s
        res = [s[0]]
        continous = 1
        for i in range(1, l):
            if s[i] == s[i-1]:
                if continous < 2:
                    continous += 1
                    res.append(s[i])
            else:
                continous = 1
                res.append(s[i])
        return "".join(res)
        