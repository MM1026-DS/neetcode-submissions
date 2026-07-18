class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(str(len(val))+'#'+val for val in strs) 

    def decode(self, s: str) -> List[str]:
        decoded = [] 
        pointer = 0 
        while pointer < len(s):
            delimiter = pointer

            while s[delimiter] != '#':
                delimiter += 1

            length = int(s[pointer:delimiter])

            string_start = delimiter + 1
            string_end = string_start + length

            decoded.append(s[string_start:string_end])

            pointer = string_end

        return decoded
