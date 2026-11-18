class Solution:
    def isValid(self, s: str) -> bool:
        d={
            '}':'{',
            ')':'(',
            ']':'['
        }
        pairs=[]
        for i in range(len(s)):
            if s[i] in '({[':
                pairs.append(s[i])
            else:
                if len(pairs)==0:
                    return False
                else:
                    if pairs[-1]==d[s[i]]:
                        pairs.pop()
                    else:
                        return False
        if len(pairs)==0:
            return True