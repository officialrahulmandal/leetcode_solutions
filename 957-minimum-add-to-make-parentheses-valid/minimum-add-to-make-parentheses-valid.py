class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter= []
        for string in s:
            if string=='(':
                counter.append(string)
            elif string == ')':
                if len(counter) > 0 and counter[-1]=='(':
                    counter.pop()
                else:
                    counter.append(string)

        return len(counter)

        