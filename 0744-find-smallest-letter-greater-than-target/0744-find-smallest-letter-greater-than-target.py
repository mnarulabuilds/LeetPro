class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ans = letters[0]

        for letter in letters:
            if ord(letter) > ord(target):
                return letter
        
        return ans
