class Solution:
    def fib(self, n: int) -> int:
        counter=1
        if n==0:
            return 0
        elif n==1:
            return 1
        elif n==2:
            return 1

        second_last = 1
        last = 1 
        
        for i in range(3, n+1):
            new_var = second_last + last
            second_last = last
            last = new_var
            

        return new_var

        