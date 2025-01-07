
#Python Solution
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        final_list = []
        mega_word = " ".join(words)
        for word in words:
            if mega_word.count(word)>1:
                final_list.append(word)
        
        return final_list