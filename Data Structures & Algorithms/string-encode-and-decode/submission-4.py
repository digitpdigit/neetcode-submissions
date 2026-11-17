class Solution:
    # The problem for encoder would be to correctly separate between items
    # Just like accept length in http rest, we can define the char length at start
    # That way, decoder always know when to put into item and when to skip
    # Oh we also need separator, in case we have > 1 digits length
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            length = len(word)
            encoded += f"{length}#" + word
        
        return encoded

    # Decoder should be able to clearly knows when to create new item and when to not
    def decode(self, s: str) -> List[str]:
        print(s)
        is_parsing = False
        temp = ""
        length = 0
        current_index = 0
        result = []

        for c in s:
            # Here we try to get the metadata
            if not is_parsing:

                # If we hit separator, we skip and record the length
                if c == "#":
                    is_parsing = True
                    length = int(temp)
                    temp = ""
                    result.append(temp)

                    if length == 0:
                        current_index += 1
                        is_parsing = False
                    continue

                temp += c
            else:
                result[current_index] += c
                length -= 1

                if length <= 0:
                    current_index += 1
                    is_parsing = False

        return result

