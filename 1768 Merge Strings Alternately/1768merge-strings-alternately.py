class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        A = len(word1)
        B = len(word2)
        a = 0
        b = 0
        ans = ""
        word = 1

        while a<A and b<B:
            if word == 1:
                ans += word1[a]
                a+=1
                word =2
            else:
                ans += word2[b]
                b += 1
                word = 1
        
        while a<A:
            ans+=word1[a]
            a+=1
        
        while b<B:
            ans += word2[b]
            b+=1
        
        return ans
