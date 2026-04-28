def isIsomorphic(s: str, t: str) -> bool: #isomorphic string 
    map_s_t = {}
    map_t_s = {}

    for cs, ct in zip(s, t):
        if cs not in map_s_t and ct not in map_t_s:
            map_s_t[cs] = ct
            map_t_s[ct] = cs
        elif map_s_t.get(cs) != ct or map_t_s.get(ct) != cs:
            return False

    return True
# Example test cases
print(isIsomorphic("egg", "add"))   # True
print(isIsomorphic("foo", "bar"))   # False
print(isIsomorphic("paper", "title"))  # True
print(isIsomorphic("ab", "aa"))    # False 