class Soluation:
    def VaildAnagram(self, s:str,t:str) -> bool:
        if len(s) != len(t):
            return False
        
        countS,countT = {},{}

        for i in range(len(s)):
            countS[s[i]]= 1+countS.get(s[i], 0)
            countT[t[i]]= 1+countT.get(t[i], 0)
        # here c hold the key of counts dict
        for c in countS:
            if countS[c] != countT.get(c,0):
                return False
        return True
    
d =  Soluation()
print(d.VaildAnagram("Ram","Ram"))
print(d.VaildAnagram("rat","rat"))
