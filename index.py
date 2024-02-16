def longestCommonPrefix(strs):
    if not strs:
        return ""
    
    prefix = strs[0]
    
    for string in strs[1:]:
        while string[:len(prefix)] != prefix:
            prefix = prefix[:len(prefix)-1]
            if not prefix:
                return ""
    
    return prefix


# UseCase:
strs = ["flower", "flow", "flight"]
print(longestCommonPrefix(strs))