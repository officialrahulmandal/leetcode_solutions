class Solution:
    def isValid(self, s: str) -> bool:
        mapping={')':'(','}':'{',']':'['}
        store=[]
        for w in s:
            if w not in mapping:
                store.append(w)
            else:
                if len(store) !=0 and store[-1]==mapping[w]:
                    store.pop()
                    continue
                else:
                    return False
        if len(store)!=0:
            return False
        return True
                

        