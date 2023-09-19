def removedoubledletter(s):
# initialize an empty string to store the result 
    result = ""
# loop through the charecters in the input string
    for i in range (len(s)):
                                           # if the current character  is not equal to the next character (or it's the last charecter),
                                           # add ity to the result string
     if i == len(s) -1 or s[i] != s[i+1]:
        result += s[i]
    return result
#example usage:
output_string=removedoubledletter("bookkeepere")
print(output_string) 
#output:"bokeper"