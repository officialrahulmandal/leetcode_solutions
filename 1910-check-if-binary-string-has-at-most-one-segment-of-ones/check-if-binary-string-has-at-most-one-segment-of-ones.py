class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        found=False
        found_One=False

        for a in s:
            if a==str(1):
                print('in')
                if not found and not found_One:
                    print('side')
                    found=True
                    found_One=True
                elif not found and found_One:
                    return False
                else:
                    continue
            else:
                if found:
                    if a!=1:
                        found=False
                
                continue
        return True

        