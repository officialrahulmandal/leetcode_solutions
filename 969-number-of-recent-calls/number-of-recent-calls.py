class RecentCounter:

    def __init__(self):
        self.store=[]
        self.start=0
        

    def ping(self, t: int) -> int:
        self.store.append(t)
        while self.store[self.start]<t-3000:
            self.start+=1
        return len(self.store)-self.start
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)