class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        # Solution 2:
        return [i for i, w in enumerate(words) if x in w]

        # Solution 1:
        res = []
        for i, word in enumerate(words):
            if x in word:
                res.append(i)
        return res