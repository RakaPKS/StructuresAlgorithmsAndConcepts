# There are three types of edits that can be performed on strings:
# - Insert a character
# - Remove a character
# - Replace a characters
# Given two strings s t, write a function to check if they are one edit or zero edits away.

# Naive solution
# Check all four cases individually
# Runtime O(n)
def naiveInsertCharacter(small, large):
    replaced = False
    for index, character in enumerate(small):
        if character != large[index] and not replaced:
            small = "".join([small[:index], large[index], small[index:]])
            replaced = True
    return small == large


def naiveReplaceCharacter(s, t):
    replaced = False
    for index, character in enumerate(s):
        if character != t[index] and not replaced:
            s = "".join([s[:index], t[index], s[index+1:]])
            replaced = True
    return s == t


def naiveOneAway(s, t) -> bool:
    # Zero edits away
    if s == t:
        return True
    # Insert a character
    if len(s) - len(t) == 1:
        return naiveInsertCharacter(t, s)
    if len(t) - len(s) == 1:
        return naiveInsertCharacter(s, t)
    if len(s) == len(t):
        return naiveReplaceCharacter(s, t)
    else:
        return False

# Optimized solution
# merge insert and replace functions


def optCharacter(s, t, equal):
    replaced = False
    for index, character in enumerate(s):
        if character != t[index] and not replaced:
            if equal:
                s = "".join([s[:index], t[index], s[index+1:]])
            else:
                s = "".join([s[:index], t[index], s[index:]])
            replaced = True
    return s == t


def optOneAway(s, t) -> bool:
    # Zero edits away
    if s == t:
        return True
    # Insert a character
    if len(s) - len(t) == 1:
        return optCharacter(t, s, False)
    if len(t) - len(s) == 1:
        return optCharacter(s, t, False)
    if len(s) == len(t):
        return optCharacter(s, t, True)
    else:
        return False


print("Naive")
# Should return True
print("\nShould Be True")
print(naiveOneAway("hello", "hello"))
print(naiveOneAway("hello", "ello"))
print(naiveOneAway("ello", "hello"))
print(naiveOneAway("hello", "herlo"))

# Should return False
print("\nShould be False")
print(naiveOneAway("hello", "worlds"))
print(naiveOneAway("worlds", "hello"))
print(naiveOneAway("welcome", "hi"))
print(naiveOneAway("hi", "welcome"))
print(naiveOneAway("hello", "world"))

print("\nOptimized")
# Should return True
print("\nShould Be True")
print(optOneAway("hello", "hello"))
print(optOneAway("hello", "ello"))
print(optOneAway("ello", "hello"))
print(optOneAway("hello", "herlo"))

# Should return False
print("\nShould be False")
print(optOneAway("hello", "worlds"))
print(optOneAway("worlds", "hello"))
print(optOneAway("welcome", "hi"))
print(optOneAway("hi", "welcome"))
print(optOneAway("hello", "world"))
