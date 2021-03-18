# Given a string s, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards and backwards.
# A permutation is a rearrangement of letters. The palindrome does not need to be limited
# to just dictionary words.

def createCountDict(s):
    countLetter = {}
    for character in s:
        if ord(character) >= 97 and ord(character) <= 122:
            if character in countLetter.keys():
                countLetter[character] += 1
            else:
                countLetter[character] = 1
    return countLetter


def checkPalindromePerm(countLetter):
    middle = ""
    for character in countLetter:
        if middle and countLetter[character] % 2 == 1:
            return False
        if countLetter[character] % 2 == 1:
            middle = character
    return True


def PalindromePermutation(s):
    s = s.lower()
    countLetter = createCountDict(s)
    return checkPalindromePerm(countLetter)


trueS = "Taco cat"
falseS = "world"
# Should return True
print(PalindromePermutation(trueS))
# Should return false
print(PalindromePermutation(falseS))
