class Solution:

    def getAnagramKey(self, string: str) -> Tuple:
        # Creating list of english letter alphabet
        alphabet_list = [0] * 26

        for s in string:
            index = ord(s) - ord("a")
            alphabet_list[index]+=1
        
        return tuple(alphabet_list)


        
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]

        result = []
        list_group = collections.defaultdict(list)

        for str_list in strs:
            key = self.getAnagramKey(str_list)
            list_group[key].append(str_list)

        for key in list_group:
            result.append(list_group[key])
        
        return result
