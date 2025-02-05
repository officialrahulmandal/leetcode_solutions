
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        sorted_a = sorted(deck)
        queue = []
        i=0
        while len(queue) != len(deck):
            #print(len(queue), len(deck))
            if len(queue)==0 or len(queue)==1:
                queue.append(sorted_a.pop())
            else:
                last = queue[0]
                del queue[0]
                queue.append(last)
                queue.append(sorted_a.pop())
        queue.reverse()
        return queue
                

        