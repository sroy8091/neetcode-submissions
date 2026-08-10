class Solution:

    def encode(self, strs: List[str]) -> str:
        encodeSub = ""
        for s in strs:
            for i in s:
                encodeSub += str(ord(i))
                encodeSub += "#"
            encodeSub += "@"
        return encodeSub

    def decode(self, s: str) -> List[str]:
        encoded = s.split("@")[:-1]
        decoded = list()
        for s in encoded:
            d = ""
            for i in s.split("#")[:-1]:
                d += chr(int(i))
            decoded.append(d)
        
        return decoded
