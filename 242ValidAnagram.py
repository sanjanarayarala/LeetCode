class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        character_count={}
        for char, char2 in zip(s, t):
            character_count[char]= character_count.get(char, 0) + 1
            character_count[char2]= character_count.get(char2, 0) - 1
        
        for count in character_count.values():
            if count != 0:
                return False

        return True

        
        