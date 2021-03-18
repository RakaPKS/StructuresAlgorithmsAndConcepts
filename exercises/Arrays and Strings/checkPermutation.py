# Given two strings s and t, write a method to decide if one
# is a permutation of the other.

# Naive solution
# O(n log n + m log m)
def naiveCheckPermutation(s, t) -> bool:
    return sorted(s) == sorted(t)

# Efficient solution
# O(n+m)


def efficientCheckPermutation(s, t) -> bool:
    if len(s) == len(t):
        scoreS = 0
        scoreT = 0
        for character in s:
            scoreS += ord(character)
        for character in t:
            scoreT += ord(character)
        return scoreS == scoreT
    return False


trueS = "god"
trueT = "dog"
falseS = "hello"
falseT = "world"

# Should return True
print(naiveCheckPermutation(trueS, trueT))
# Should return False
print(naiveCheckPermutation(falseS, falseT))
# Should return True
print(efficientCheckPermutation(trueS, trueT))
# Should return False
print(efficientCheckPermutation(falseS, falseT))
