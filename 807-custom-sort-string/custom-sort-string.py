class Solution(object):
    def customSortString(self, order, s):
        char_count = {char: 0 for char in order}
        print(char_count)
        for char in s:
            if char in char_count:
                char_count[char] += 1
        print(char_count)
    
        sorted_s = ''
        for char in order:
            sorted_s += char * char_count[char]
        
        for char in s:
            if char not in order:
                sorted_s += char
        print(sorted_s)
    

        return sorted_s
        