class Solution:
    def reverseVowels(self, s: str) -> str:
        l = 0
        r = len(s) - 1
        vowels = {'a','e','i','o','u','A','E','I','O','U'}
        new_list = list(s)

        while l < r:
            if new_list[l] in vowels and new_list[r] in vowels:
                new_list[l] , new_list[r] = new_list[r] , new_list[l]
                l += 1
                r -= 1
            elif new_list[l] in vowels and new_list[r] not in vowels:
                r -= 1
            elif new_list[l] not in vowels and new_list[r] in vowels:
                l += 1
            else:
                l += 1
                r -= 1
        return "".join(new_list)