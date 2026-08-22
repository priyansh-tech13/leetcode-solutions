class Solution:
    def checkPerfectNumber(self, num):
        if num <= 1:
            return False

        c = 1

        i = 2
        while i * i <= num:
            if num % i == 0:
                c += i

                if i != num // i:
                    c += num // i

            i += 1

        return c == num