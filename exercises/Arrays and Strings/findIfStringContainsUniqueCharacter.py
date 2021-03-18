# Given string inputString:
# Find if the the string contains only unique characters

# Naive
# Runtime O(n^2)
def naiveFind(inputString) -> bool:
    for index, character in enumerate(inputString):
        for otherCharacter in inputString[index+1:]:
            if character == otherCharacter:
                return False
    return True


# Efficient without any data structures
# Runtime O(n log n)
def efficientNoDataStructuresFind(inputString) -> bool:
    inputString = sorted(inputString)
    for index, character in enumerate(inputString):
        if index == len(inputString)-1:
            return True
        if character == inputString[index+1]:
            return False


# Efficient find
# runtime O(n)
def efficientFind(inputString) -> bool:
    dictionary = {}
    for character in inputString:
        if ord(character) in dictionary:
            return False
        else:
            dictionary[ord(character)] = character
    return True


correct = "world"
incorrect = "hello"

# Should return True
print(naiveFind(correct))
print(efficientNoDataStructuresFind(correct))
print(efficientFind(correct))

# Should return False
print(naiveFind(incorrect))
print(efficientNoDataStructuresFind(incorrect))
print(efficientFind(incorrect))
