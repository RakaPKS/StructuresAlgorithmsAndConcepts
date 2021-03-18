# Assume you have a method isSubstring which checks if one word
# is a substring of another.
# Given two strings s and t, write code to check if t
# is a rotation of s using only one call to isSubstring()

def isSubstring(s, sub):
    return sub in s


def stringRotation(s, t):
    if len(s) == len(t):
        return isSubstring(s+s, t)
    return False


s = "waterbottle"
t = "bottlewater"
z = "bottlwater"

print(stringRotation(s, t))
print(stringRotation(s, z))
