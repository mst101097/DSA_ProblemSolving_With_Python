class Soluation:
    def VaildAnagram(self, s:str,t:str) -> bool:
        # method 3 with sorted method 
        #return sorted(s) == sorted(t)
        
        #method 2 with inbuild counter function
        #return Counter(s) == Counter(t)
        
        # method 1
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
