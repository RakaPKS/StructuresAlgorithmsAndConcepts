# implement a method to perform basic string compression using the
# counts of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3.
# if the compressed string would not become smaller then return the original string
# string only has upper and lower case characters

def stringCompression(s):
    changed = False
    currentChar = ""
    count = 0
    output = ""
    for character in s:
        if currentChar == character:
            count += 1
            changed = True
        else:
            if currentChar:
                output += currentChar + str(count)
            currentChar = character
            count = 1
    return output if changed else s


print(stringCompression("abc"))
print(stringCompression("aabcccccaaa"))
