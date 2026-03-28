class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        _s = []
        _t = []
        for ch in s:
            if ch == '#':
                if len(_s) > 0:
                    _s.pop()
            else:
                _s.append(ch)
        
        for ch in t:
            if ch == '#':
                if len(_t) > 0:
                    _t.pop()
            else:
                _t.append(ch)

        return _s == _t