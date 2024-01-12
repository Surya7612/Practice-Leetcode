# class Solution:
#     # def isPalindrome(self, s: str) -> bool:
#     #     clean_string = ''.join(char.lower() for char in s if char.isalnum())
#     #here it checks the reverse string with the given string but that isn't the correct way, we have to check for the mirror-ness inside the string itself.
#     #     return clean_string == clean_string[::-1]
#     def isPalindrome(self, s: str) -> bool:
#         left, right = 0, len(s) - 1

#         while left < right:
#             # Skip non-alphanumeric characters
#             while left < right and not s[left].isalnum():
#                 left += 1
#             while left < right and not s[right].isalnum():
#                 right -= 1

#             # Compare characters
#             if s[left].lower() != s[right].lower():
#                 return False

#             left += 1
#             right -= 1

#         return True

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [c.lower() for c in s if c.isalnum()]
        return all (s[i] == s[~i] for i in range(len(s)//2))
        #for the above for loop, the range works till the half of the length of the string as we only need to check for the first half as the rest is the mirror of it.

        
