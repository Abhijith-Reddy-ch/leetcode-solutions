class Solution:
    def isHappy(self, n: int) -> bool:
        st = set()

        while n != 1:
            if n in st:
                return False
            st.add(n)

            num = 0
            while n > 0:
                digit = n % 10
                num += digit * digit
                n //= 10

            n = num

        return True
