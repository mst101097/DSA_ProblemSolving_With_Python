'''
This problem is simliar to the Fabanoice series...
'''

class Soluation:
    def cliambingStairs(self, n:int) -> int:
        one , two = 1 , 1

        for i in range(n - 1):
            temp = one
            one = one + two
            two =  temp 
        
        return one
obj = Soluation()
result  = obj.cliambingStairs(n=6)

print("Result steps :",result)