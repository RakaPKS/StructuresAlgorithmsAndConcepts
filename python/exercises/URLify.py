# Write a method to replace all spaces in a string s with '%20'.
# You my asume that the string has sufficient space at the end to hold
# the additional characters, and that you are given the "true"
# length of the string.

# Naive Solution (In this case the less beautiful solution)
# Runtime O(n)
def naiveURLify(s):
    outputString = ""
    for character in s:
        if character == " ":
            outputString += "%20"
        else:
            outputString += character
    return outputString


# Efficient
# Runtime O(n)
def efficientUrlify(s):
    return s.replace(" ", "%20")


inputString = "Hello world! How are we doing?"
print(naiveURLify(inputString))
print(efficientUrlify(inputString))
