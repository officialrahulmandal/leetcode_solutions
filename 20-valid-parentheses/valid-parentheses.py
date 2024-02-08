class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        array=[]
        for value in s:
            if value=='(' or value=='{' or value=='[':
                array.append(value)
            elif len(array)==0:
                return False
            elif value=='}':
                if array[-1]=='{':
                    array.pop()
                else:
                    return False
            elif value==')':
                if array[-1]=='(':
                    array.pop()
                else:
                    return False

            elif value==']':
                if array[-1]=='[':
                    array.pop()
                else:
                    return False
        if len(array)==0:
            return True
        else:
            return False

        