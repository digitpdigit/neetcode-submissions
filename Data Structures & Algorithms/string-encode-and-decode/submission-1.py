class Solution:

    def encode(self, strs: List[str]) -> str:
        # The basic rules would be int#string
        result = ""

        for string in strs:
            result += str(len(string)) + "#" + string
        
        return result

    def decode(self, s: str) -> List[str]:
        # walk throught the string and parse
        # 5#Hello
        is_parsing = False
        temp = ""
        length = 0
        result = []

        for char in s: 
            if not is_parsing:
                if char == "#":
                    is_parsing = True
                    length = int(temp)
                    temp = ""
                    
                    if length == 0:
                        result.append("")
                        is_parsing = False
                
                    continue
                temp += char
            else:
                temp += char
                if len(temp) == length:
                    is_parsing = False
                    result.append(temp)
                    temp = ""
            
            

        return result
