class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dictionary = {}
        for string in strs:
            key = ''.join(sorted(string))
            if key not in dictionary.keys():
                dictionary[key] = [string]
            else:
                dictionary[key].append(string)

        return list(dictionary.values())
