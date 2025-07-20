class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        word_dict=defaultdict(list)
        
        for s in strs:
            sorted_word= ''.join(sorted(s))
            word_dict[sorted_word].append(s)

        return list(word_dict.values())

            
            

        