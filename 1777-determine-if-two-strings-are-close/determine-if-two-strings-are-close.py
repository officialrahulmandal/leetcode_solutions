class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1)!=len(word2):
            return False
        freq1={}
        freq2={}
        for w1 in word1:
            if w1 in freq1:
                freq1[w1]+=1
            else:
                freq1[w1]=1
        
        for w2 in word2:
            if w2 in freq2:
                freq2[w2]+=1
            else:
                freq2[w2]=1
        
        if set(freq1.keys())!=set(freq2.keys()):
            return False
        if sorted(freq1.values())!=sorted(freq2.values()):
            return False
        return True