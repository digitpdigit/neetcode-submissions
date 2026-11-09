class Solution:
    def anagramToKey(self, string: str) -> str:
        char_index = [0] * 26
        
        for c in string:
            index = ord(c) - ord('a')
            char_index[index] += 1
        
        return "".join(map(str, str(char_index)+"."))

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # In case we wanna have a cache to not recalculate two string
        string_to_key = {}
        # To store result
        key_to_array = {}
        # Final result
        result = []

        # To group those, we need to make the string represented as key
        # For example, im thinking of using array of number, contain information of the index and occurences
        # For example act = 10100000000000000001000000
        # a = first index and occur once
        # c = third index and occur once
        # we can iterate and group on one go

        for string in strs:
            if string in string_to_key:
                key = string_to_key[string]
            else:
                key = self.anagramToKey(string)

            if key in key_to_array:
                key_to_array[key].append(string)
            else:
                key_to_array[key] = [string]

        # Create result 
        for _, array in key_to_array.items():
            result.append(array)
           
            
        return result
