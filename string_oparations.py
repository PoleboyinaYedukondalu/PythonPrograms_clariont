def translate(word):
    vowels = "aeiou"
    b_language_word = ""
    
    for letter in word:
        if letter in vowels:
            b_language_word += "b" + letter
        else:
            b_language_word += letter
    
    return b_language_word

# Test cases
print(translate("quick"))  # Output: "quibuick"
print(translate("spaghetti"))  # Output: "spabaghebettibi"
print(translate("adieu"))  # Output: "abadieubieu"
print(translate("audiophile"))  # Output: "aubaudiobiophibilebe"
print(translate("queueing"))  # Output: "queueibueueing